from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegSerialier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserLogSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)