from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpRequest
from json import loads
from .serializer import UserRegSerialier, UserLogSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class RegistrationView(APIView):
    def post(self, request: HttpRequest):
        data = loads(request.body)
        data_serializer =  UserRegSerialier(data=data)
        if not data_serializer.is_valid():
            return Response(status=400)
        User(**data_serializer.data).save()
        return Response(status=200)

class LoginView(APIView):
    def post(self, request: HttpRequest):
        data = loads(request.body)
        data_serializer = UserLogSerializer(data)
        if not data_serializer.is_valid():
            return Response(status=400)
        user = authenticate(username=data_serializer.data['username'],
                            password=data_serializer.data['password'])
        if user is None:
            return Response(status=400)
        login(request, user)
        return Response(status=200)

class LogoutView(APIView):
    def post(self, request: HttpRequest):
        logout(request)
        return Response(status=200)
