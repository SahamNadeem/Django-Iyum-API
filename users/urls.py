from django.contrib import admin
from django.urls import include, path
from . import views
from rest_framework import routers

urlpatterns = [
    path(r'^/users',views.UserListView),
    path('/myspi', views.home),
    path(r'^/UserAPIView',views.UserAPIView)
]