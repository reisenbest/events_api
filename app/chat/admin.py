from django.contrib import admin
from .models import MessageHistory, ChatRooms

@admin.register(MessageHistory)
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at','room')
    search_fields = ('user', 'content', 'room')
    list_filter = ('created_at', 'room')


@admin.register(ChatRooms)
class ChatRoomsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


