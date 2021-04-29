from django.shortcuts import render
from rest_framework import viewsets
from .models import Record
from .serializers import RecordSerializer
from django_filters.rest_framework import DjangoFilterBackend

class RecordView(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seller', 'buyer']

