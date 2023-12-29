from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Record
from .serializers import RecordSerialzer
from rest_framework.pagination import LimitOffsetPagination
from .pagination import MyCursorPagnition
# Create your views here.

class RecordCreate(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerialzer
    #pagination_class = LimitOffsetPagination
    pagination_class = MyCursorPagnition
    
    