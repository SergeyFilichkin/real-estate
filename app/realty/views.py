from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Flat


class AllFlatsApi(APIView):
    def get(self, request):
        data = Flat.objects.all().values()
        return Response({'flats': list(data)})


class FlatApi(APIView):
    def get(self, request, flat_id):
        try:
            flat = Flat.objects.get(id=flat_id)
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
        except:
            return Response({'error': 'Object does not exists'})
