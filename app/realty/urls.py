from django.conf.urls.static import static
from django.urls import path

from config import settings
from .views import (FlatListApi, FlatDetailApi)
                    # FloorListView, FloorDetailView, BuildingListView, BuildingDetailView)

urlpatterns = [
    path('flats/', FlatListApi.as_view()),
    path('flats/<int:flat_id>/', FlatDetailApi.as_view()),
    # path('floors/', FloorListView.as_view()),
    # path('floors/<int:pk>/', FloorDetailView.as_view()),
    # path('buildings/', BuildingListView.as_view()),
    # path('buildings/<int:building_id>/', BuildingDetailView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
