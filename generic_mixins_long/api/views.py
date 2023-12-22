from django.shortcuts import render
from .models import Record
from .serializers import RecordSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
# Create your views here.

class RecordListView(GenericAPIView, ListModelMixin):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class RecordCreateView(GenericAPIView, CreateModelMixin):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class RecordRetriveView(GenericAPIView, RetrieveModelMixin):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class RecordDeleteView(GenericAPIView, DestroyModelMixin):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class RecordUpdateView(GenericAPIView, UpdateModelMixin):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)   
    