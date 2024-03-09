from rest_framework import serializers


class FlatSerializer(serializers.Serializer):
    square = serializers.FloatField()
    living_space = serializers.FloatField()
    kitchen_area = serializers.FloatField()
    rooms = serializers.IntegerField()
    status = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    photo = serializers.ImageField()
    floor = serializers.IntegerField(source='floor.number')


class FloorSerializer(serializers.Serializer):
    name = serializers.CharField()
    number = serializers.IntegerField()
    flats = FlatSerializer(many=True)

    def to_representation(self, instance):
        data = {
            'name': instance['name'],
            'number': instance['number'],
            'flats': [FlatSerializer(flat).data for flat in instance['flats']]
        }

        return data
