from django.shortcuts import render
from rest_framework import viewsets
from .models import Record
from .serializers import RecordSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import DjangoObjectPermissions, IsAuthenticated, IsAdminUser
from .custompermssion import MyPermission
# Create your views here.
class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    
    