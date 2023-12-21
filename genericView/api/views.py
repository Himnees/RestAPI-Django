from .models import Record
from .serializers import RecordSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
# Create your views here.


class RecordRetriveView(GenericAPIView, RetrieveModelMixin):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class RecordRUDView(GenericAPIView, DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)   
    
class RecordCUview(GenericAPIView, CreateModelMixin, ListModelMixin):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)