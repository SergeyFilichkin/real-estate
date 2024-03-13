from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count

from .models import Flat, Floor, Building


class FlatSelector:
    @staticmethod
    def get_all_flats():
        return Flat.objects.all().select_related('floor', 'category')

    @staticmethod
    def get_flat_by_id(flat_id):
        flat = Flat.objects.filter(id=flat_id).select_related('floor', 'category').first()
        return flat


class FloorSelector:
    @staticmethod
    def get_floors_with_total_flats():
        floors = Floor.objects.annotate(total_flats=Count('flat'))
        return floors

    @staticmethod
    def get_floor_detail(pk):
        try:
            floor = Floor.objects.get(id=pk)
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            return None
        flats = list(floor.flat_set.all().select_related('floor', 'category'))
        data = {
            'id': floor.id,
            'name': floor.name,
            'number': floor.number,
            'flats': flats
        }
        return data


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

        data = {
            'id': building.id,
            'floors': building.floors,
            'name': building.name,
            'date_of_construction': building.date_of_construction,
            'date_of_delivery': building.date_of_delivery,
            'address': building.address,
            'number': building.number,
            'status': building.status,
            'type': building.type,
            'has_parking': building.has_parking,
            'elevators': building.elevators,
            'total_flats': total_flats
        }
        return data
