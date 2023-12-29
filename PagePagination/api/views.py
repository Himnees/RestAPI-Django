from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Record
from .serializers import RecordSerialzer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class RecordCreate(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerialzer
    pagination_class = PageNumberPagination
    # page size is set in setting.py
    