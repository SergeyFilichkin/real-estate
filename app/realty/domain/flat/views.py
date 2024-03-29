from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .selector import FlatSelector


class FlatListView(APIView):
    class FlatSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        square = serializers.FloatField()
        living_space = serializers.FloatField()
        kitchen_area = serializers.FloatField()
        rooms = serializers.IntegerField()
        status = serializers.CharField()
        price = serializers.IntegerField()
        description = serializers.CharField()
        photo = serializers.ImageField()
        floor = serializers.CharField()

    def get(self, request):
        all_flats = FlatSelector.get_all_flats()
        return Response(data=self.FlatSerializer(all_flats.all_flats, many=True).data)


class FlatDetailView(APIView):
    class FlatSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        square = serializers.FloatField()
        living_space = serializers.FloatField()
        kitchen_area = serializers.FloatField()
        rooms = serializers.IntegerField()
        status = serializers.CharField()
        price = serializers.IntegerField()
        description = serializers.CharField()
        photo = serializers.ImageField()
        floor = serializers.CharField()
        category = serializers.CharField()

    def get(self, request, flat_id):
        flat = FlatSelector.get_flat_by_id(flat_id)
        if not flat:
            return Response({'error': 'Object does not exist'})

        return Response(data=self.FlatSerializer(flat).data)
