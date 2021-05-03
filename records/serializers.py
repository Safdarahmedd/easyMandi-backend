from rest_framework import serializers
from .models import Record, Live

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['address', 'seller', 'harvest', 'amount', 'Quantity', 'buyer', 'date', 'description']

class LiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Live
        fields = ['address', 'seller', 'isTerminated']
