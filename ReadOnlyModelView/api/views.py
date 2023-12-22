from .models import Record
from .serializers import RecordSerializer
from rest_framework import viewsets

# Create your views here.

class RecordReadOnlyMedoleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer