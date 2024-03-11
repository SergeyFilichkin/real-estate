from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count

from .models import Flat, Floor


class FlatSelector:
    @staticmethod
    def get_all_flats():
        return Flat.objects.all()

    @staticmethod
    def get_flat_by_id(flat_id):
        flat = Flat.objects.filter(id=flat_id).first()
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
        flats = list(floor.flat_set.all())
        data = {
            'name': floor.name,
            'number': floor.number,
            'flats': flats
        }
        return data
