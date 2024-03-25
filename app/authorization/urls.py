from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from .views import *

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='registeruser'),

    path('login/', UserLoginView.as_view(), name='login'),

    path('logout/', UserLogoutView.as_view(), name='login'),

    # path('test/', ExampleView.as_view(), name='login'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
