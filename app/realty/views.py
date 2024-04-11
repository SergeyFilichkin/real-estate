from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from realty.selectors import FlatSelector


class FlatListAPI(APIView):
    class FlatListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField(max_length=120)
        price = serializers.IntegerField()
        overall_square = serializers.IntegerField()
        living_square = serializers.IntegerField()
        rooms = serializers.IntegerField()
        view_from_windows = serializers.CharField()
        lavatory = serializers.IntegerField()
        level = serializers.IntegerField()
        elevator = serializers.IntegerField()
        year_of_sale = serializers.IntegerField()
        parking = serializers.CharField()
        is_complete = serializers.BooleanField()
        has_kitchen = serializers.BooleanField()

    def get(self, request):
        flats = FlatSelector.flat_list()

        data = self.FlatListSerializer(flats, many=True).data

        return Response(data)
