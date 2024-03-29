from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from realty.domain.building.entities import DetailBuildingEntity, ListBuildingsEntity, BuildingEntity
from realty.models.building import Building


class BuildingSelector:
    @staticmethod
    def get_all_buildings():
        buildings = Building.objects.all()
        buildings_entities = [
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
                project=building.project
            )
            for building in buildings
        ]

        data = ListBuildingsEntity(all_buildings=buildings_entities)

        return data

    @staticmethod
    def get_building_detail(pk):
        try:
            building = Building.objects.get(id=pk)
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            return None
        total_flats = Building.objects.get(pk=pk).flat_set.count()

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
            project=building.project,
            total_flats=total_flats
        )
        return data
