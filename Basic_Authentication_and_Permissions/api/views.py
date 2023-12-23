from django.shortcuts import render
from rest_framework import viewsets
from .models import Record
from .serializers import RecordSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
# Create your views here.
class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticated]
    #permission_classes = [IsAdminUser]
