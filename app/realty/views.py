from django.shortcuts import render
from rest_framework import generics
from .models import Flat
from .serializers import FlatSerializer

class FlatListCreateAPIView(generics.ListCreateAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer

class FlatRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer

