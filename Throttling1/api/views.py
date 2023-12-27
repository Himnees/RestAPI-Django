from django.shortcuts import render
from rest_framework import viewsets
from .models import Record
from .serializer import RecordSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throthling import JackRateThrottle
# Create your views here.

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    #throttle_classes = [JackRateThrottle]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
