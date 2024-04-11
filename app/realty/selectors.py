from realty.models import Flat


def flat_list():
    flats = Flat.objects.all()

    return flats
