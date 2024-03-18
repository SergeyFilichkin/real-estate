from django.urls import path

from .views import BuildingListView, BuildingDetailView

urlpatterns = [
    path('buildings/', BuildingListView.as_view()),
    path('buildings/<int:building_id>/', BuildingDetailView.as_view())
]
