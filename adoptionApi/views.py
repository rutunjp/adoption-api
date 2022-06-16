from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import viewsets, filters
from django.shortcuts import render
from .serializers import AnimalSerializer
from django_filters.rest_framework import DjangoFilterBackend


from .models import  Animal
# Create your views here.

class AnimalViewSet(viewsets.ModelViewSet,generics.ListAPIView):
    queryset=Animal.objects.all().order_by('id')
    serializer_class=AnimalSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['name', 'animal','gender']
    search_fields=['name','gender']
 