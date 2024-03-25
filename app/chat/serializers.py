from rest_framework import serializers
from .models import MessageHistory, ChatRooms


class ChatRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRooms
        fields = ['id', 'title', 'description', ]


class MessageHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageHistory
        fields = ['user', 'content', 'created_at', 'room']
