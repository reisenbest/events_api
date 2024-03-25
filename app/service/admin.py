from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# Register your models here.

@admin.register(Organizations)
class OrganizationsAdmin(admin.ModelAdmin):
    list_display = ['title', 'adress', 'postcode']
    list_filter = ['title', 'adress', 'postcode']
    search_fields = ['title', 'adress', 'postcode']


class EventsAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'organizations', 'image', 'show_image', 'date']
    list_display = ('title', 'description', 'show_image', 'date')
    readonly_fields = ['show_image']
    search_fields = ['title', 'description']
    list_filter = ['date']

    @admin.display(description='Миниатюра изображения мероприятия', ordering='content')
    def show_image(self, event: Events):
        if event.image:
            return mark_safe(f"<img src='{event.image.url}' width=80> ")
        return 'Фото отсутствует'


admin.site.register(Events, EventsAdmin)
