from rest_framework import serializers

from realty.models import Floor


class FlatSerializer(serializers.Serializer):
    square = serializers.FloatField()
    living_space = serializers.FloatField()
    kitchen_area = serializers.FloatField()
    rooms = serializers.IntegerField()
    status = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    photo = serializers.ImageField()
    floor_id = serializers.PrimaryKeyRelatedField(queryset=Floor.objects.all())
