from django.urls import path

from regions.views import TownCreateListView, RegionUpdateDeleteView, RegionTownListView, RegionCreateListView

app_name = 'regions'

urlpatterns = [
    path('', RegionCreateListView.as_view(), name='list-create'),
    path('<int:pk>/', RegionUpdateDeleteView.as_view(), name='update-delete'),

    path('towns/', TownCreateListView.as_view(), name='town-list-create'),
    path('towns/<int:pk>/', TownCreateListView.as_view(), name='town-update-delete'),
    path('<int:region_id>/towns/', RegionTownListView.as_view(), name='town-list-by-region'),
]