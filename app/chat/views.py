from chat.docs import *
from django.http import Http404, JsonResponse
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatRooms
from rest_framework import viewsets
from .models import ChatRooms
from .serializers import ChatRoomsSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


@docs_for_chat_CRUD
class ChatRoomsViewSet(viewsets.ModelViewSet):
    queryset = ChatRooms.objects.all()
    serializer_class = ChatRoomsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'title'



from drf_spectacular.utils import extend_schema

@entry_chat_schema
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):

    return render(request, "chat/index.html")


@chat_schema
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def room(request, room_name):

    try:
        chat_room = ChatRooms.objects.get(title=room_name)
    except ChatRooms.DoesNotExist:
        return JsonResponse({"error": "Чата с таким названием не существует"}, status=404)

    return render(request, "chat/room.html", {"room_name": room_name})