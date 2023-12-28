from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Record
from .serializers import RecordSerializer
# Create your views here.
class RecordViewSet(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city']
    