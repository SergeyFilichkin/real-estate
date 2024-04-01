from realty.domain.flat.entities import FlatEntity
from realty.models.flat import Flat


class FlatSelector:
    @staticmethod
    def get_all_flats():
        flats = Flat.objects.all().select_related('floor', 'category', 'building')
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
                floor_number=flat.floor.number,
                category_name=flat.category.name,
                building_name=flat.building.name
            )
            for flat in flats
        ]

        return data

    @staticmethod
    def get_flat_by_id(flat_id):
        flat = Flat.objects.select_related('floor', 'category', 'building').get(id=flat_id)
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
            floor_number=flat.floor.number,
            category_name=flat.category.name,
            building_name=flat.building.name
        )
        return data
