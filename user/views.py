from django.shortcuts import render
from rest_framework import generics,mixins
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework import filters
# Create your views here.
class UserListCreate(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['=username']