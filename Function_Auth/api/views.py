from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Record
from .serliazers import RecordSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
#@api_view()
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def RecordAPI(request,pk):
    if request.method == 'GET':
        pk = request.data.get('id')
        
        if pk is not None:
            stu = Record.objects.get(pk=id)
            serializer = RecordSerializer(stu)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
 
    
    
    
    if request.method == 'PUT':
        id =request.data.get('id')
        id = pk
        stu = Record.objects.get(pk=id)
        serializer = RecordSerializer(stu, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'}, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        id = request.data.get('id')
        id = pk
        stu = Record.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_200_OK)

@api_view(['GET','POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def RecordAPI(request):
    if request.method == 'GET':
        stu = Record.objects.all()
        serializer = RecordSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)