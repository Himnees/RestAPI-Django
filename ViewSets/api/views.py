from .models import Record
from .serializers import RecordSerializer
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class RecordViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Record.objects.all()
        serializer = RecordSerializer(stu, many = True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def retrieve(self, request, pk=None):
        id = pk
        if pk is not None:
            stu = Record.objects.get(pk=id)
            serializer = RecordSerializer(stu)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        id = pk
        stu = Record.objects.get(pk=id)
        serializer = RecordSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    
    def partial_update(self, request, pk=None):
        id = pk
        stu = Record.objects.get(pk=id)
        serializer = RecordSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Partially Updated'})
        return Response(serializer.errors)
    
    
    def delete(self, request, pk=None):
        id = pk
        stu = Record.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})