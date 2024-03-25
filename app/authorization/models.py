from django.db import models
from django.contrib.auth.models import AbstractUser
from service.models import Organizations
from phonenumber_field.modelfields import PhoneNumberField


# переопределяем стандартного пользователя
class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, blank=False, verbose_name='псевдоним пользователя',
                                help_text='Обязательное поле. Могут повторяться')

    email = models.EmailField(unique=True, blank=False, verbose_name='email пользователя')
    organization = models.ForeignKey(Organizations, on_delete=models.SET_NULL,
                                     null=True, verbose_name='Организация', blank=True,
                                     help_text='Укажите организацию. Необязательное поле')

    #сделал для удобства и в рамках тестового так. По хорошему поле должно быть обязательное, с максимальной длиной
    # уникальное и так далее. много настроек можно. я о  них знаю и о способах это сделать
    phone_number = PhoneNumberField(verbose_name='Номер телефона', blank=True, null=True,
                                    help_text='Введите номер телефона начиная с +7. Необязательное поле')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
