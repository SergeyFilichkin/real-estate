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


class BaseFloorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    number = serializers.IntegerField()


class ListFloorSerializer(BaseFloorSerializer):
    total_flats = serializers.IntegerField()


class DetailFloorSerializer(BaseFloorSerializer):
    flats = FlatSerializer(many=True)
