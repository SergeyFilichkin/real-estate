from rest_framework import serializers


class ListBuildingSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    floors = serializers.IntegerField()
    name = serializers.CharField()
    date_of_construction = serializers.DateField()
    date_of_delivery = serializers.DateField()
    address = serializers.CharField()
    number = serializers.IntegerField()
    status = serializers.CharField()
    type = serializers.CharField()
    has_parking = serializers.BooleanField()
    elevators = serializers.IntegerField()


class DetailBuildingSerializer(ListBuildingSerializer):
    total_flats = serializers.IntegerField()
