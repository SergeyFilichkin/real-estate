from django.shortcuts import render
from rest_framework import viewsets
from .models import Flat
from .serializers import FlatSerializer

class FlatViewSet(viewsets.ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer
