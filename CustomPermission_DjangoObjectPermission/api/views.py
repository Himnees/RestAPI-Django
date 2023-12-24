from django.shortcuts import render
from rest_framework import viewsets
from .models import Record
from .serializers import RecordSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import DjangoObjectPermissions
from .custompermssion import MyPermission
# Create your views here.
class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]
    
    