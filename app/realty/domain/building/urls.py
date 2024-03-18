from django.urls import path

from .views import BuildingListView, BuildingDetailView

building_list = path('buildings/', BuildingListView.as_view())
building_detail = path('buildings/<int:building_id>/', BuildingDetailView.as_view())
