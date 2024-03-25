from rest_framework import serializers
from .models import Organizations, Events
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class OrganizationsSerializer(serializers.ModelSerializer):
    '''
    сериалайзер для реализации пункта 1 из ТЗ
    1.	Создание организации
    '''
    class Meta:
        model = Organizations
        fields = ['pk', 'title', 'description', 'adress', 'postcode']


class UserPhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['pk', 'email', 'phone_number']


class OrganizationSerializerForEvents(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = ['pk', 'title', 'adress', 'postcode']

class EventSerializer(serializers.ModelSerializer):
    #  кастомный сериалайзер для вывода всех мероприятий + организаций, которые с ними связаны в ключе organizations_details
    organizations = serializers.PrimaryKeyRelatedField(queryset=Organizations.objects.all(), many=True)
    organizations_details = OrganizationSerializerForEvents(source='organizations', read_only=True, many=True)

    class Meta:
        model = Events
        fields = ['pk', 'title', 'description', 'organizations', 'organizations_details', 'image', 'date']


