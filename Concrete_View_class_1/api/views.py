from .models import Record
from .serializers import RecordSerializer
from rest_framework.generics import ListAPIView,CreateAPIView ,ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, DestroyAPIView

# Create your views here.
class RecordList(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    
class RecordCreate(CreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    
class RecordRetrieve(RetrieveAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    
class RecordUpdate(UpdateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class RecordDelete(DestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    
class RecordListCreate(ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    
class RecordRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    
class RecordRetrieveDelete(RetrieveDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer