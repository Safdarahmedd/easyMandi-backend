from django.shortcuts import render
from rest_framework import viewsets
from .models import Record
from .serializers import RecordSerializer

class RecordView(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


