from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Record
from .serializers import RecordSerialzer
from .pagination import MyPagePagination
# Create your views here.

class RecordCreate(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerialzer
    pagination_class = MyPagePagination
    # page size is set in setting.py
    