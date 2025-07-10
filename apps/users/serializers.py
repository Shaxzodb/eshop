# users/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import BotUser

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'default': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        user.is_staff = True  # faqat adminlar
        user.save()
        return user

class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = '__all__'



