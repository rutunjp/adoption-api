from rest_framework import viewsets
from django.shortcuts import render
from .serializers import AnimalSerializer
from .models import  Animal
# Create your views here.

class AnimalViewSet(viewsets.ModelViewSet):
    queryset=Animal.objects.all().order_by('name')
    serializer_class=AnimalSerializer