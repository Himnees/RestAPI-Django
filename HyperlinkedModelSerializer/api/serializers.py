from rest_framework import serializers
from .models import Record

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ['id','url','name','roll','city']
        