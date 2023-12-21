from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Record
from .serliazers import RecordSerializer
# Create your views here.
#@api_view()
@api_view(['GET','POST','PUT','DELETE'])
def RecordAPI(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Record.objects.get(id=id)
            serializer = RecordSerializer(stu)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            stu = Record.objects.all()
            serializer = RecordSerializer(stu, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        id =request.data.get('id')
        stu = Record.objects.get(pk=id)
        serializer = RecordSerializer(stu, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'}, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Record.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_200_OK)
        