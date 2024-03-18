from rest_framework.response import Response
from rest_framework.views import APIView

from .selector import FlatSelector
from .serializers import FlatSerializer


class FlatListView(APIView):
    def get(self, request):
        all_flats = FlatSelector.get_all_flats()
        return Response(data=FlatSerializer(all_flats, many=True).data)


class FlatDetailView(APIView):
    def get(self, request, flat_id):
        flat = FlatSelector.get_flat_by_id(flat_id)
        if not flat:
            return Response({'error': 'Object does not exist'})

        return Response(data=FlatSerializer(flat).data)
