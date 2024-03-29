from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count

from realty.domain.flat.entities import FlatEntity
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
        flats = floor.flat_set.all().select_related('floor', 'category')
        data_flats = [
            FlatEntity(
                id=flat.id,
                square=flat.square,
                living_space=flat.living_space,
                kitchen_area=flat.kitchen_area,
                rooms=flat.rooms,
                status=flat.status,
                price=flat.price,
                description=flat.description,
                photo=flat.photo,
                floor=flat.floor,
                category=flat.category,
                building=flat.building
            )
            for flat in flats
        ]

        data = FloorEntity(
            id=floor.id,
            name=floor.name,
            number=floor.number,
            flats=data_flats
        )
        return data
