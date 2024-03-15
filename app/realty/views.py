from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .selectors import FlatSelector, FloorSelector, BuildingSelector, ProjectSelector
from .serializers import FlatSerializer, DetailFloorSerializer, ListFloorSerializer, ListBuildingSerializer, DetailBuildingSerializer, ProjectSerializer, DetailProjectSerializer


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


class ProjectListView(APIView):
    def get(self, request):
        all_projects = ProjectSelector.get_all_projects()
        return Response(data=ProjectSerializer(all_projects, many=True).data)


class ProjectDetailView(APIView):
    def get(self, request, project_id):
        project = ProjectSelector.get_project_detail(project_id)
        if not project:
            return Response({'error': 'Object does not exist'})

        return Response(data=DetailProjectSerializer(project).data)
