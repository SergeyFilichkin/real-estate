from rest_framework.response import Response
from rest_framework.views import APIView

from .selector import BuildingSelector
from .serializers import ListBuildingSerializer, DetailBuildingSerializer


class BuildingListView(APIView):
    def get(self, request):
        all_buildings = BuildingSelector.get_all_buildings()
        return Response(data=ListBuildingSerializer(all_buildings, many=True).data)


class BuildingDetailView(APIView):
    def get(self, request, building_id):
        building = BuildingSelector.get_building_detail(building_id)
        if not building:
            return Response({'error': 'Object does not exist'})

        return Response(data=DetailBuildingSerializer(building).data)
