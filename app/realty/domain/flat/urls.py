from django.urls import path

from .views import FlatListView, FlatDetailView

urlpatterns = [
    path('', FlatListView.as_view()),
    path('<int:flat_id>/', FlatDetailView.as_view())
]