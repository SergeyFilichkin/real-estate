from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Flat
from .serializers import FlatSerializer


class AllFlatsApi(APIView):
    def get(self, request):
        data = Flat.objects.all()
        return Response({'flats': FlatSerializer(data, many=True).data})


class FlatDetailView(APIView):
    def get(self, request, flat_id):
        try:
            flat = Flat.objects.get(id=flat_id)
        except:
            return Response({'error': 'Object does not exists'})

        return Response({'flat': {
            'square': flat.square,
            'living_space': flat.living_space,
            'kitchen_area': flat.kitchen_area,
            'rooms': flat.rooms,
            'floor': flat.floor,
            'status': flat.status,
            'price': flat.price,
            'description': flat.description,
            'photo': flat.photo.url}
            }
        )
