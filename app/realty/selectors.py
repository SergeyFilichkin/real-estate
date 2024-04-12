from realty.models import Flat


class FlatSelector:
    @staticmethod
    def flat_list():
        flats = Flat.objects.all()

        return flats

    def get_flat(self, pk):
        flat = Flat.objects.get(pk)

        return flat
