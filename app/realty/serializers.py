from rest_framework import serializers


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
    floor = serializers.IntegerField(source='floor.number')
    category = serializers.CharField(source='category.name')


class BaseFloorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    number = serializers.IntegerField()


class ListFloorSerializer(BaseFloorSerializer):
    total_flats = serializers.IntegerField()


class DetailFloorSerializer(BaseFloorSerializer):
    flats = FlatSerializer(many=True)


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
