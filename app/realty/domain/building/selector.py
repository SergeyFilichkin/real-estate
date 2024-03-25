from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from .entities import BuildingEntity
from realty.models.building import Building
from realty.models.flat import Flat


class BuildingSelector:
    @staticmethod
    def get_all_buildings():
        buildings = Building.objects.all()
        return buildings

    @staticmethod
    def get_building_detail(pk):
        try:
            building = Building.objects.get(id=pk)
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            return None
        total_flats = Flat.objects.select_related('building').filter(building_id=pk).count()

        data = BuildingEntity(
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
            total_flats=total_flats
        )
        return data
