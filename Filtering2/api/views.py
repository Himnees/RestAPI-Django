from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Record
from .serializers import RecordSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class RecordViewSet(ListAPIView):
    queryset = Record.objects.all()
    #queryset = Record.objects.filter(passby = 'user1')
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Record.objects.filter(passby = user)
    