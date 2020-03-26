from mptt.utils import get_cached_trees
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from regions.models import Region, Town
from regions.serializers import TownListSerializer, RegionListSerializer, RegionUpdateSerializer
from utils.views import CustomUpdateAPIView


class RegionMixin:
    permission_classes = (IsAuthenticated,)
    queryset = Region.objects.all()
    serializer_class = RegionListSerializer


class RegionCreateListView(RegionMixin, ListCreateAPIView):
    """
    Список всех регионов в виде дерева и добавление новых регионов
    """
    def list(self, *args, **kwargs):
        tree = get_cached_trees(Region.objects.filter(level=0))
        serializer = RegionListSerializer(tree, many=True)
        return Response(serializer.data)


class RegionUpdateDeleteView(RegionMixin, CustomUpdateAPIView, DestroyAPIView):
    """
    Управления справочником регионов: изменение/удаление
    """
    update_serializer = RegionUpdateSerializer


class TownMixin:
    permission_classes = (IsAuthenticated,)
    queryset = Town.objects.all()
    serializer_class = TownListSerializer


class TownCreateListView(TownMixin, ListCreateAPIView):
    """
    Просмотр всех городов в виде списка
    """
    pass


class TownUpdateDeleteView(TownMixin, UpdateAPIView, DestroyAPIView):
    """
    Управления справочником городов: изменение/удаление
    """
    pass


class RegionTownListView(TownMixin, ListAPIView):
    """
    Просмотр городов региона в виде списка
    """

    def get_queryset(self):
        qs = super().get_queryset()
        regions = Region.objects.filter(pk=self.kwargs.get('region_id')).get_descendants(include_self=True)
        region_ids = regions.values_list('pk', flat=True)
        return qs.filter(region__in=region_ids)
