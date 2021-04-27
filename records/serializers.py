from rest_framework import serializers
from .models import Record

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['seller', 'harvest', 'amount', 'Quantity', 'buyer', 'date', 'description']