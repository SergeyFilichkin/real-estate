from django.http import JsonResponse
from django.views.generic import ListView

from realty.models import Flat


class FlatsListView(ListView):
    model = Flat

    def get(self, request, *args, **kwargs):
        super.get(request, *args, **kwargs)

        response = []

        for flat in self.object_list():
            response.append({
                "id": flat.id,
                "name": flat.name,
                "price": flat.price,
                "overall_square": flat.overall_square,
                "rooms": flat.rooms,
                "view_from_windows": flat.view_from_windows,
                "lavatory": flat.lavatory,
                "level": flat.level,
                "elevator": flat.elevator,
                "year_of_sale": flat.year_of_sale,
                "parking": flat.parking,
                "is_complete": flat.is_complete,
                "is_kitchen": flat.is_kitchen,

            })

        return JsonResponse(response, safe=False)