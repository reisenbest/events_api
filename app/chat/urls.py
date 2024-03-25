from django.urls import path
from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatRoomsViewSet

router = DefaultRouter()
router.register(r'chat-rooms', ChatRoomsViewSet)


urlpatterns = [
    path('api/', include(router.urls)), #CRUD для моделей чат рума

    path('chat/', index, name='chat'), #путь к выбору комнаты
    path("chat/<str:room_name>/", room, name="room"), #сам чат
]
