from django.urls import path

from .views import FloorListView, FloorDetailView

floor_list = path('floors/', FloorListView.as_view())
floor_detail = path('floors/<int:pk>/', FloorDetailView.as_view())
