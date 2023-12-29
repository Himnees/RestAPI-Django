from rest_framework.serializers import ModelSerializer
from .models import Record

class RecordSerialzer(ModelSerializer):
    class Meta:
        model = Record
        fields = ['id','name','roll','city']
        