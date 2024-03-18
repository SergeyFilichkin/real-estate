from rest_framework import serializers

from realty.domain.flat.serializers import FlatSerializer


class BaseFloorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    number = serializers.IntegerField()


class ListFloorSerializer(BaseFloorSerializer):
    total_flats = serializers.IntegerField()


class DetailFloorSerializer(BaseFloorSerializer):
    flats = FlatSerializer(many=True)
