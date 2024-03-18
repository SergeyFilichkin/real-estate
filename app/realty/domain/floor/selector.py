from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count

from realty.models.floor_model import Floor


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
