from .models import Record
from .serializers import RecordSerializer
from rest_framework.generics import ListAPIView,CreateAPIView ,ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, DestroyAPIView

# Create your views here.
class RecodListCreate(ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    
class RecordRUD(RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer