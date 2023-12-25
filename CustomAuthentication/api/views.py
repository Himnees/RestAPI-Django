from django.shortcuts import render
from rest_framework import viewsets
from .models import Record
from .serializers import RecordSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .authentication import CustomAuthentication
# Create your views here.

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
    