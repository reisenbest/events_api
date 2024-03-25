from datetime import datetime
import json

from chat.serializers import MessageHistorySerializer

from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from .models import MessageHistory, ChatRooms

UserModel = get_user_model()


class ChatConsumer(GenericAsyncAPIConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        # Получаем информацию о текущем пользователе из базы данных
        await self.get_user()

        await self.accept()

        await self.chat_group_message()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Получаем текущего пользователя
        user = await self.get_user()

        # получаем адрес электронной почты текущего пользователя
        user_email = user.email

        # получаем название комнаты
        room = await self.get_room_name()

        # создаем сообщение
        final_message = f"{user_email}: {message} (отправлено: {datetime.now()})"

        # отправляем сообщение в ххранилище историй сообщейний

        await self.archive_message(user, message, room)

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": final_message}
        )

    async def chat_message(self, event):
        message = event["message"]

        await self.send(text_data=json.dumps({"message": message}))

    async def chat_group_message(self):
        '''

        функция выводит на экран историю предыдущих сообщений именно этой комнаты
        '''

        room = self.room_name
        message_history = await self.show_message_history(room)
        for message in message_history:
            user = message['user']
            contetn = message['content']
            created_at = message['created_at']
            await self.send(text_data=json.dumps({"message": f"{user}: {contetn} (отправлено: {created_at})"}))

    @database_sync_to_async
    def get_user(self):
        '''
        :return: возвращает текущего юзера
        '''
        current_user = UserModel.objects.get(email=self.scope['user'].email)
        return current_user

    @database_sync_to_async
    def get_room_name(self):
        '''

        :return: возвращает комнату
        '''
        current_room = ChatRooms.objects.get(title=self.room_name)
        return current_room

    @database_sync_to_async
    def archive_message(self, user, message, room):
        '''
        архивация сообщения
        :param user: текущий юзер
        :param message: текст сообщения
        :param room: текущая комната
        '''
        message = MessageHistory.objects.create(user=user, content=message, room=room)
        return message

    @database_sync_to_async
    def show_message_history(self, room):
        '''
        :param room: текущая комната
        :return: отдает сериализованные данные из бд где хранятся все отправленные
        сообщения чтобы вывести их для пользователя
        '''
        messages = MessageHistory.objects.filter(room__title=room)
        serializer = MessageHistorySerializer(messages, many=True)
        serialized_data = serializer.data

        return serialized_data
