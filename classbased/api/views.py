from django.shortcuts import render
from rest_framework import generics
from .models import Category
from .serializers import CategorySerialzier



# Create your views here.

class CategoryList(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerialzier

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all() 
    serializer_class=CategorySerialzier