from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import PostSerializer
from rest_framework import viewsets
from .models import Posts
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_auth.views import UserDetailsView

# Create your views here.
class PostListView(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
