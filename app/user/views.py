from django.shortcuts import render
from rest_framework import generics
from user.serializer import UserSerializer,AuthTokenSerializers
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class=UserSerializer
    

class CreateTokenView(ObtainAuthToken):
    serializer_class=AuthTokenSerializers