from django.db.models import Count
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Flat, Floor
from .serializers import FlatSerializer, DetailFloorSerializer, ListFloorSerializer


class FlatListView(APIView):
    def get(self, request):
        data = Flat.objects.all()
        return Response(data=FlatSerializer(data, many=True).data)


class FlatDetailView(APIView):
    def get(self, request, flat_id):
        try:
            flat = Flat.objects.get(id=flat_id)
        except:
            return Response({'error': 'Object does not exists'})

        return Response(data=FlatSerializer(flat).data)


class FloorListView(APIView):
    def get(self, request):
        floors = Floor.objects.annotate(total_flats=Count('flat'))
        data = ListFloorSerializer(floors, many=True).data
        return Response(data)


class FloorDetailView(APIView):
    def get(self, request, pk):
        try:
            floor = Floor.objects.get(id=pk)
        except:
            return Response({'error': 'Object does not exists'})

        flats = list(Flat.objects.filter(floor=pk))
        data = DetailFloorSerializer({
            'name': floor.name,
            'number': floor.number,
            'flats': flats
        }).data

        return Response(data)
