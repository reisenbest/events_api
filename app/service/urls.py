from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('users-phones/', ListUsersPhoneNumbersAPIView.as_view(), name='phonenumbers-list'),
    # список  юзеров и их телефонных

    path('organization/', CreateOrganizationAPIView.as_view(), name='organization-create'),  # создание организации

    path('event/', CreateEventAPIView.as_view(), name='event-create'),  # создание мероприятия

    path('event/<int:pk>/', EventWithDetailedInfoAPIView.as_view(), name='event-detail'),
    # детальная инфа о мероприятии

    path('eventslist/', ListEventsAPIView.as_view(), name='events-list')  # список мероприятий
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
