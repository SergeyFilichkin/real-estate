from django.urls import path

from .views import FloorListView, FloorDetailView

urlpatterns = [
    path('floors/', FloorListView.as_view()),
    path('floors/<int:pk>/', FloorDetailView.as_view())
]