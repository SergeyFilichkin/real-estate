from django.urls import path

from .views import FlatListView, FlatDetailView

flat_list = path('flats/', FlatListView.as_view())
flat_detail = path('flats/<int:flat_id>/', FlatDetailView.as_view())
