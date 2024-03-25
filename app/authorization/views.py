from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model, authenticate, login, logout
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import UserSerializer, UserLoginSerializer
from .docs import *


class CreateUserView(CreateAPIView):
    #регистрация нового пользователя
    model = get_user_model()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    @user_stub_schema
    def get(self, request):
        return Response({'detail: ': 'Для регистрации отправьте post запрос с данными  на этот адрес'})

    @user_create_schema
    def post(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            email = response.data['email']
            return Response({'detail:': f'Пользователь с email: {email} создан'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserLoginView(CreateAPIView):
    model = get_user_model()
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    @user_stub_schema
    def get(self, request):
        return Response({'detail: ': 'Для авторизации отправьте post запрос с данными  на этот адрес'})

    @user_login_schema
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        email = request.data['email']
        password = request.data['password']
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'detail': f'Пользователь {email} авторизован',
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': f'пользователь {email} не найден'}, status=status.HTTP_404_NOT_FOUND)


class UserLogoutView(APIView):
    # authentication_classes = [JWTAuthentication] для удобства тестов здесь убрал, чтобы не надо было идти в сваггер все время
    permission_classes = [IsAuthenticated]

    @user_logout_schema
    def get(self, request):
        user = request.user

        logout(request)
        return Response({'message': f'Пользователь {user} разлогинен'}, status=status.HTTP_200_OK)
from django.conf import settings
#
# class ExampleView(APIView):
#     # authentication_classes = [JWTAuthentication]
#     permission_classes = [AllowAny]
#
#     def get(self, request):
#         print(settings.MEDIA_URL, settings.MEDIA_ROOT)
#         content = {'message': 'Hello, World!'}
#         return Response(content)
