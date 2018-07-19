from django.contrib import admin
from django.urls import include, path
from . import views
from rest_framework import routers

urlpatterns = [
    path('/posts',views.PostListView),
    path('/PostListViewopen', views.PostListView)
]