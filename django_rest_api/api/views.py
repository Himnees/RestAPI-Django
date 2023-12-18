from django.shortcuts import render, HttpResponse
from .models import Record
from .serializers import RecordSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
# Create your views here.

# Single API
def APIView(request,pk):
    stu = Record.objects.get(id=pk)
   # print(stu)
    serializer = RecordSerializer(stu)
    print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')
    #return JsonResponse(serializer.data)

#All (querset)
def APIViewall(request):
    stu = Record.objects.all()
    serializer = RecordSerializer(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)