from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name','last_name','is_active')
