from django.db import models


# Create your models here.

class Organizations(models.Model):
    title = models.CharField(max_length=255, verbose_name='название', blank=False)
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    adress = models.CharField(max_length=255, verbose_name='адрес', blank=False)
    postcode = models.CharField(max_length=10, verbose_name='почтовый индекс', blank=False)

    class Meta:
        verbose_name = 'Организации'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return f'{self.title}'


class Events(models.Model):
    title = models.CharField(max_length=255, verbose_name='название', blank=False)
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    organizations = models.ManyToManyField(Organizations, verbose_name='Организации',
                                           related_name='events', blank=True, null=True)
    #возможно было бы лучше через url field чтобы с апи удобнее работать, но в тз сказано было именно хранить.
    #поэтому файлом
    #добавлять лучше через админ панель
    #или json в base64 через эндпоинт
    image = models.ImageField(upload_to='events_images/', verbose_name='изображение для мероприятия',
                              blank=True, null=True)
    date = models.DateField(verbose_name='Дата мероприятия',
                            help_text='Укажите дату мероприятия',
                            blank=True,
                            null=True)

    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return f'{self.title}'
