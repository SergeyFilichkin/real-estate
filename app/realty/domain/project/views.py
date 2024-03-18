from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .selector import ProjectSelector
from ...models.building import Building


class ProjectListView(APIView):
    class ProjectListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        description = serializers.CharField()

    def get(self, request):
        all_projects = ProjectSelector.get_all_projects()
        data = self.ProjectListSerializer(all_projects, many=True).data
        return Response(data)


class ProjectDetailView(APIView):
    class BuildingsSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        floors = serializers.IntegerField()
        name = serializers.CharField()
        date_of_construction = serializers.DateField()
        date_of_delivery = serializers.DateField()
        address = serializers.CharField()
        number = serializers.IntegerField()
        status = serializers.CharField()
        type = serializers.CharField()
        has_parking = serializers.BooleanField()
        elevators = serializers.IntegerField()

    class ProjectDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        description = serializers.CharField()
        buildings = serializers.SerializerMethodField()

        def get_buildings(self, project):
            buildings_data = Building.oblects.filter(project_id=id)
            serializer = self.BuildingsSerializer(buildings_data, many=True)
            return serializer.data

    def get(self, request, project_id):
        project = ProjectSelector.get_project_detail(project_id)
        if not project:
            return Response({'error': 'Object does not exist'})

        return Response(data)
