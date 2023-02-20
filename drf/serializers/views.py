from django.shortcuts import render
from .models import Quotes
from .serializers import QuotesSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser


# Create your views here.
@ csrf_exempt
def quotes_detail(request):
    if request.method=='GET':
        data=Quotes.objects.all()
        serializer=QuotesSerializer(data,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    elif request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=QuotesSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            response={'msg':'Data Created'}
            json_data=JSONRenderer().render(response)
            return HttpResponse(json_data,content_type='application/json')
        return HttpResponse('something went wrong')
    
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        print(id)
        data=Quotes.objects.get(id=id)
        serializer=QuotesSerializer(data,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            response={'msg':'Data is updated'}
            json_data=JSONRenderer().render(response)
            return HttpResponse(json_data,content_type='application/json')
        return HttpResponse('something went wrong')
    
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        data=Quotes.objects.get(id=id)
        data.delete()
        response={'msg': 'Data is Deleted'}
        json_data=JSONRenderer().render(response)
        return HttpResponse(json_data,content_type='application/json')




