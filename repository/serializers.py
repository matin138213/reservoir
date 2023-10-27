from rest_framework import serializers
from .models import User, Password

class PasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Password
        fields = ['id', 'title', 'password', 'description']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.get('password', instance.password)
        instance = super().update(instance, validated_data)
        instance.set_password(password)
        instance.save()
        return instance
