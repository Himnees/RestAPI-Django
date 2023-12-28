from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Record
from .serializers import RecordSerializer
from rest_framework.filters import SearchFilter
# Create your views here.
class RecordViewSet(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_backends = [SearchFilter]
    # search_fields = ['city','name']
    search_fields = ['city']