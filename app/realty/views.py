from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FlatSerializer
from .models import Flat
from django.http import Http404


class FlatListAPIView(APIView):

    def get(self, request, format=None):
        flats = Flat.objects.all()
        serializer = FlatSerializer(flats, many=True)
        return Response(serializer.data)


class FlatDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Flat.objects.get(pk=pk)
        except Flat.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        flat = self.get_object(pk)
        serializer = FlatSerializer(flat)
        return Response(serializer.data)