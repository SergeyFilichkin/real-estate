from rest_framework.response import Response
from rest_framework.views import APIView

from .selector import FloorSelector
from .serializers import ListFloorSerializer, DetailFloorSerializer


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
