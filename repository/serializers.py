from rest_framework import serializers
from .models import User, Password


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = ['id', 'title', 'password', 'description', 'user']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'username', 'password']
