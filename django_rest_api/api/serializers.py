from rest_framework import serializers

class RecordSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=200)