from rest_framework import serializers

from regions.models import Town, Region
from utils.serializers import RecursiveField, update_nested


class TownListSerializer(serializers.ModelSerializer):
    region = serializers.IntegerField(source='region_id')

    class Meta:
        model = Town
        fields = ('id', 'name', 'region')

    def validate(self, attrs):
        return super().validate(attrs)

    def update(self, instance, validated_data):
        region = validated_data['region']
        if isinstance(region, Region):
            validated_data['region'] = region.pk
        return super().update(instance, validated_data)


class RegionListSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True, required=False)
    towns = TownListSerializer(many=True, required=False)

    class Meta:
        model = Region
        fields = ('id', 'name', 'parent', 'children', 'towns')

    def update(self, instance: Region, validated_data):
        towns = update_nested(TownListSerializer, validated_data.pop('towns', []))
        # regions = update_nested(RegionListSerializer, validated_data.pop('children', []))
        # regions = validated_data.pop('children', [])
        # serializer = TownListSerializer(many=True, data=towns, partial=True)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # TownListSerializer().update()
        instance.towns.set(towns)
        # instance.children.set(regions)

        return super().update(instance, validated_data)



