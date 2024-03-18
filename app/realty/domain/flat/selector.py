from realty.models.flat import Flat


class FlatSelector:
    @staticmethod
    def get_all_flats():
        return Flat.objects.all().select_related('floor', 'category')

    @staticmethod
    def get_flat_by_id(flat_id):
        flat = Flat.objects.filter(id=flat_id).select_related('floor', 'category').first()
        return flat
