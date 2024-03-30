from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count

from realty.domain.building.entities import BuildingEntity
from realty.domain.project.entities import ProjectEntity
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
        buildings = project.building_set.all().prefetch_related('project').annotate(total_flats=Count('flat'))

        data = ProjectEntity(
            id=project.id,
            name=project.name,
            description=project.description,
            buildings=[
                BuildingEntity(
                    id=building.id,
                    floors=building.floors,
                    name=building.name,
                    date_of_construction=building.date_of_construction,
                    date_of_delivery=building.date_of_delivery,
                    address=building.address,
                    number=building.number,
                    status=building.status,
                    type=building.type,
                    has_parking=building.has_parking,
                    elevators=building.elevators,
                    project_name=building.project.name
                )
                for building in buildings
            ]
        )

        return data
