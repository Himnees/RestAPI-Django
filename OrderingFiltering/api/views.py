from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Record
from .serializers import RecordSerializer
from rest_framework.filters import OrderingFilter
# Create your views here.
class RecordViewSet(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_backends = [OrderingFilter]
    #ordering_fields = ['name','city']
    #ordering_fields = '__all__'