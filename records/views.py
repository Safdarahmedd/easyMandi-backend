from django.shortcuts import render
from rest_framework import viewsets
from .models import Record, Live
from .serializers import RecordSerializer, LiveSerializer
from django_filters.rest_framework import DjangoFilterBackend

class RecordView(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seller', 'buyer']

class LiveView(viewsets.ModelViewSet):
    queryset = Live.objects.all()
    serializer_class = LiveSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seller', 'address', 'isTerminated']
