from rest_framework import serializers

from regions.models import Town, Region
from utils.serializers import RecursiveField


class TownListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Town
        fields = ('id', 'name', 'region')


class RegionListSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True, required=False)
    towns = TownListSerializer(many=True, required=False)

    class Meta:
        model = Region
        fields = ('id', 'name', 'parent', 'children', 'towns')


class RegionUpdateSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True, required=False)
    towns = TownListSerializer(many=True, required=False)

    class Meta:
        model = Region
        fields = ('id', 'name', 'parent', 'children', 'towns')

    def update(self, instance: Region, validated_data):
        return self.update_regions(validated_data, region=instance)

    def update_regions(self, data, region=None):
        # Обновление городов региона
        self.update_towns(data.pop('towns', []))
        # Обноление региона
        region = self.update_region(data, region)
        # Обновление дочерних регионов (рекурсией)
        children = data.pop('children', [])
        for region_data in children:
            self.update_regions(region_data)
        return region

    def update_region(self, data, region):
        if not region:
            region = Region.objects.get(pk=data['id'])
        region.name = data['name']
        parent = data.get('parent')
        if parent and isinstance(parent, int):
            parent = Region.objects.get(pk=parent)
        region.parent = parent
        region.save()
        return region

    def update_towns(self, towns_list):
        towns = []
        for town_data in towns_list:
            if isinstance(town_data['region'], int):
                town_data['region'] = Region.objects.get(pk=town_data['region'])
            towns.append(Town(**town_data))
        Town.objects.bulk_update(towns, ['name', 'region'])
