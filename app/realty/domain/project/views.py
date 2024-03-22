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
    class ProjectDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        description = serializers.CharField()
        buildings = serializers.IntegerField()

    def get(self, request, project_id):
        project = ProjectSelector.get_project_detail(project_id)
        if not project:
            return Response({'error': 'Object does not exist'})

        return Response(data=self.ProjectDetailSerializer(project).data)