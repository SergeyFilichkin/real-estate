from django.urls import path

from .views import FlatListView, FlatDetailView

urlpatterns = [
    path('flats/', FlatListView.as_view()),
    path('flats/<int:flat_id>/', FlatDetailView.as_view())
]