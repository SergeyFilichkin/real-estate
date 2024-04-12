from realty.models import Flat


class FlatSelector:
    @staticmethod
    def flat_list():
        flats = Flat.objects.all()

        return flats

    @staticmethod
    def get_flat(pk):
        flat = Flat.objects.get(pk)

        return flat
