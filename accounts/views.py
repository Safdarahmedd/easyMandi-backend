from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']