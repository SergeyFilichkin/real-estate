from realty.domain.flat.entities import FlatEntity
from realty.models.flat import Flat


class FlatSelector:
    @staticmethod
    def get_all_flats():
        flats = Flat.objects.all().select_related('floor', 'category')
        data = [
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

        return data

    @staticmethod
    def get_flat_by_id(flat_id):
        flat = Flat.objects.select_related('floor', 'category').get(id=flat_id)
        data = FlatEntity(
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
        return data
