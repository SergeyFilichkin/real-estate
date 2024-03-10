from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .selectors import FlatSelector, FloorSelector

from .serializers import FlatSerializer, DetailFloorSerializer, ListFloorSerializer


class FlatListView(APIView):
    def get(self, request):
        data = FlatSelector.get_all_flats()
        return Response(data=FlatSerializer(data, many=True).data)


class FlatDetailView(APIView):
    def get(self, request, flat_id):
        data = FlatSelector.get_flat_by_id(flat_id)
        if not data:
            return Response({'error': 'Object does not exist'})

        return Response(data=FlatSerializer(data).data)


class FloorListView(APIView):
    def get(self, request):
        data = FloorSelector.get_floors_with_total_flats()
        return Response(data=ListFloorSerializer(data, many=True).data)


class FloorDetailView(APIView):
    def get(self, request, pk):
        data = FloorSelector.get_floor_detail(pk)
        if not data:
            return Response({'error': 'Object does not exist'})

        return Response(data=DetailFloorSerializer(data).data)
