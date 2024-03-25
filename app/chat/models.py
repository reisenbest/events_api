from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

UserModel = get_user_model()


class ChatRooms(models.Model):
    '''
    храним комнаты
    '''
    title = models.CharField(max_length=100, unique=True, blank=False,
                             verbose_name='Название комнаты')
    description = models.TextField(blank=False, default='Отсутствует', verbose_name='Описание')

    class Meta:
        verbose_name = 'Чат-румы'
        verbose_name_plural = 'Чат-румы'

    def __str__(self):
        return self.title


class MessageHistory(models.Model):
    '''
    храним историю сообщений
    '''
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE,
                             verbose_name='Пользователь', to_field='email')
    content = models.CharField(max_length=255, blank=True,
                               null=True, verbose_name='Сообщение')
    created_at = models.DateTimeField(verbose_name='Время отправки', auto_now_add=True)
    room = models.ForeignKey(ChatRooms, on_delete=models.CASCADE, verbose_name='Чат-комната')

    class Meta:
        verbose_name = 'История сообщений'
        verbose_name_plural = 'История сообщений'

    def __str__(self):
        return self.content
