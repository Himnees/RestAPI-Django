from rest_framework import serializers
from .models import Record

class RecordSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Record.objects.create(**validated_data)