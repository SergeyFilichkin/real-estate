from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from realty.models.building import Building
from realty.models.project import Project


class ProjectSelector:
    @staticmethod
    def get_all_projects():
        projects = Project.objects.all()
        return projects

    @staticmethod
    def get_project_detail(pk):
        try:
            project = Project.objects.get(id=pk)
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            return None
        buildings = Building.objects.select_related('project').filter(project_id=pk)

        data = {
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'buildings': buildings
        }

        return data
