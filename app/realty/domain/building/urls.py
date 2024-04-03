from django.urls import path

from .views import BuildingListView, BuildingDetailView

urlpatterns = [
    path('', BuildingListView.as_view()),
    path('<int:building_id>/', BuildingDetailView.as_view())
]
