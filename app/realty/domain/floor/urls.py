from django.urls import path

from .views import FloorListView, FloorDetailView

urlpatterns = [
    path('', FloorListView.as_view()),
    path('<int:pk>/', FloorDetailView.as_view())
]
