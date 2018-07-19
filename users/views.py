import view as view
from django.contrib.sites import requests
from django.shortcuts import render
from numpy.distutils.fcompiler import none
from requests import Response
from rest_framework.views import APIView

from users import services
from .serializers import UserSerializer #, LoginSerializer
from rest_framework import viewsets, request, generics
from rest_framework.response import Response
from django.contrib.auth.models import User
#from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_framework.authentication import TokenAuthentication
from rest_auth.registration.views import SocialLoginView
from rest_auth.serializers import TokenSerializer

# Create your views here.
def home(request, format=None):
    response = request.Get.get('http://localhost:8080/phppy/API.php?data=user')
    geodata = response.json()
    return Response(geodata)

class UserListView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserAPIView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

