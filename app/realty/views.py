from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Flat
from .serializers import FlatSerializer


class FlatListView(APIView):
    def get(self, request):
        data = Flat.objects.all()
        return Response(data=FlatSerializer(data, many=True).data)


class FlatDetailView(APIView):
    def get(self, request, flat_id):
        try:
            flat = Flat.objects.get(id=flat_id)
        except ObjectDoesNotExist:
            return Response({'error': 'Object does not exists'})

        return Response(data=FlatSerializer(flat).data)
