from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile
from rest_framework import serializers
from .serializers import SignupSerializer, LoginSerializer
from django_filters.rest_framework import DjangoFilterBackend



@api_view(['POST',])
def signupview (request):
    if request.method == 'POST':
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.create(serializer.validated_data)       
        else:
            data = serializer.errors
        return Response(account)

@api_view(['POST',])
def loginview (request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        data = request.data        
        if serializer.is_valid():
            info = serializer.to_internal_value(data)
            user = auth.authenticate(username=data['username'],password=data['password'])
            if user is not None:
                id = user.id 
                instance = Profile.objects.get(pk=id)
                s = serializer.to_representation(instance)
                return Response(s)
            else :
                raise serializers.ValidationError({'password': 'Incorrect password'})


 