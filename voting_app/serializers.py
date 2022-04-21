from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'password', 'last_login', 'is_superuser', 'username', 'is_staff', 'date_joined')

