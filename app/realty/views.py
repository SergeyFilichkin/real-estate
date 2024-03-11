from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .selectors import FlatSelector, FloorSelector
from .serializers import FlatSerializer, DetailFloorSerializer, ListFloorSerializer


class FlatListView(APIView):
    def get(self, request):
        all_flats = FlatSelector.get_all_flats()
        return Response(data=FlatSerializer(all_flats, many=True).data)


class FlatDetailView(APIView):
    def get(self, request, flat_id):
        flat = FlatSelector.get_flat_by_id(flat_id)
        if not flat:
            return Response({'error': 'Object does not exist'})

        return Response(data=FlatSerializer(flat).data)


class FloorListView(APIView):
    def get(self, request):
        all_floors = FloorSelector.get_floors_with_total_flats()
        return Response(data=ListFloorSerializer(all_floors, many=True).data)


class FloorDetailView(APIView):
    def get(self, request, pk):
        floor = FloorSelector.get_floor_detail(pk)
        if not floor:
            return Response({'error': 'Object does not exist'})

        return Response(data=DetailFloorSerializer(floor).data)
