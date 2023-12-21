from rest_framework import serializers
from .models import Record

def start_with_n(value):
    if value[0].lower() != 'n':
        raise serializers.ValidationError("Name should start with N ")

class RecordSerializer(serializers.Serializer):   
    name = serializers.CharField(max_length=100, validators=[start_with_n])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Record.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    # field_level validation
    def validate_roll(self, value):
        if value>=200:
            raise serializers.ValidationError('Seat Full sorry')
        return value
    
    #Object level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        
        if nm.lower()=='nabha' and ct.lower()!='bangalore':
            raise serializers.ValidationError('City must be Bangalore')
        return data