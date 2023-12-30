from .models import Record
from .serializers import RecordSerializer
from rest_framework import viewsets

# Create your views here.

class RecordMedoleViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer