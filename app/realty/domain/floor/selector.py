from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count

from realty.domain.floor.entities import FloorEntity
from realty.models.floor import Floor


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
        data = FloorEntity(
            id=floor.id,
            name=floor.name,
            number=floor.number,
            flats=flats
        )
        return data
