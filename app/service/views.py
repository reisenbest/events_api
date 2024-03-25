from adrf.views import APIView
from asgiref.sync import sync_to_async
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from service.filters import EventsFilter
from .serializers_1part import *
from .serializers_2part import OneEventSerializerWithDetailedInfo
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import CustomPagination
from .docs import *
import asyncio


UserModel = get_user_model()


@user_list_docs
class ListUsersPhoneNumbersAPIView(ListAPIView):
    '''
    реализация задания из ТЗ
    2.	Реализовать возможность хранения номера телефона пользователя
    '''
    queryset = UserModel.objects.all()
    serializer_class = UserPhoneNumberSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserPhoneNumberSerializer(queryset, many=True)
        return Response(serializer.data)


@organization_create_docs_post
class CreateOrganizationAPIView(CreateAPIView):
    '''
    реализация задания из ТЗ
    1.	Создание организации
    '''
    model = Organizations
    permission_classes = [IsAuthenticated]
    serializer_class = OrganizationsSerializer
    authentication_classes = [JWTAuthentication]

    @organization_create_docs_get
    def get(self, request):
        return Response({'detail: ': 'Для создания организации отправьте post запрос с данными  на этот адрес'})


from asgiref.sync import sync_to_async


class CreateEventAPIView(APIView):
    '''
    Реализация задания из ТЗ
    2. Создание мероприятия
    При создании мероприятия необходимо использовать sleep 60 секунд и данный запрос не должен быть блокирующим.
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    authentication_classes = [JWTAuthentication]

    @sync_to_async
    def create_event_instance(self, serializer):
        if serializer.is_valid():
            return serializer.save()
        else:
            return None

    @event_create_docs_post
    async def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        await asyncio.sleep(60)

        event_instance = await self.create_event_instance(serializer)
        if event_instance:
            return Response({'message': 'Мероприятие успешно создано', 'event_id': event_instance.id},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@event_detail_docs
class EventWithDetailedInfoAPIView(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    '''
    реализация задания из ТЗ
    3.	Вывод мероприятия с информацией о всех действующих пользователей, которые участвуют в организации мероприятия
     с разбивкой по организациям (вывести информацию о организации с объединением почтового индекса и адресом).
    '''
    permission_classes = [IsAuthenticated]
    queryset = Events.objects.all()
    serializer_class = OneEventSerializerWithDetailedInfo


@event_list_docs
class ListEventsAPIView(ListAPIView):
    '''
    реализация задания из ТЗ
    4.  Вывод мероприятий с возможностью фильтрации и сортировки по дате,
     поиском по названию и лимитной пагинацией.
    '''
    queryset = Events.objects.all()
    serializer_class = OneEventSerializerWithDetailedInfo
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = EventsFilter
    pagination_class = CustomPagination
    search_fields = ['title']
    ordering_fields = ['date']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.paginator.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
