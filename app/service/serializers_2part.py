from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Organizations, Events

'''
вынес выполнение пункта 
3.	Вывод мероприятия с информацией о всех действующих пользователей, которые участвуют в организации мероприятия 
с разбивкой по организациям (вывести информацию о организации с объединением почтового индекса и адресом).

отдельно для удобства. Разделил на два файла отдельно сериализаторы для конечных точек под номером 1  2  в ТЗ
отдельный для пункта 3 и 4
'''

UserModel = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    # берем нужные данные о пользователях
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'phone_number', 'organization']


class OrganizationSerializer(serializers.ModelSerializer):
    # берем нужные данные об организации
    # не понял что значило "вывести информацию о организации с объединением почтового индекса и адресом"
    # вывел раздельно
    users = serializers.SerializerMethodField()

    class Meta:
        model = Organizations
        fields = ['id', 'title', 'postcode', 'users']

    def get_users(self, obj):
        # получаем всех пользователей, связанных с данной организацией
        users = obj.customuser_set.all()

        # создаем экземпляр сериализатора  для сериализации пользователей
        user_serializer = CustomUserSerializer(users, many=True)

        # вВозвращаем сериализованные данные пользователей
        return user_serializer.data


class OneEventSerializerWithDetailedInfo(serializers.ModelSerializer):
    organizations = OrganizationSerializer(many=True, read_only=True)

    class Meta:
        model = Events
        fields = ['pk', 'title', 'description', 'organizations', 'image', 'date']
