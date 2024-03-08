from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Flat, Floor
from .serializers import FlatSerializer, FloorSerializer


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
        floors = Floor.objects.all()
        data = []

        for floor in floors:
            floor_data = FloorSerializer(floor).data
            flat_data = FlatSerializer(floor.flat_set.all(), many=True).data
            floor_data['flats'] = flat_data
            data.append(floor_data)

        return Response(data)


class FloorDetailView(APIView):
    def get(self, request, pk):
        try:
            floor = Floor.objects.get(id=pk)
        except:
            return Response({'error': 'Object does not exists'})

        flat = Flat.objects.filter(floor=pk)

        data = {
            'floor': FloorSerializer(floor).data,
            'flats': FlatSerializer(flat, many=True).data
        }

        return Response(data)
