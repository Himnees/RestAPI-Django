from django.shortcuts import render
from rest_framework import viewsets
from .models import Record
from .serializers import RecordSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly,DjangoModelPermissions,DjangoObjectPermissions

# Create your views here.
class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    authentication_classes = [SessionAuthentication]
    #permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticated]
    #permission_classes = [IsAdminUser]
    #permission_classes = [DjangoModelPermissions]
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    permission_classes = [DjangoObjectPermissions]
    
    