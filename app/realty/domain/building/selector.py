from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from realty.domain.building.entities import DetailBuildingEntity, BuildingEntity
from realty.models.building import Building


class BuildingSelector:
    @staticmethod
    def get_all_buildings():
        buildings = Building.objects.select_related('project').all()
        data = [
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

        return data

    @staticmethod
    def get_building_detail(pk):
        try:
            building = Building.objects.prefetch_related('project').get(id=pk)
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            return None
        total_flats = building.flat_set.count()

        data = DetailBuildingEntity(
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
            project_name=building.project.name,
            total_flats=total_flats
        )

        return data
