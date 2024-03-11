from django.conf.urls.static import static
from django.urls import path

from config import settings
from .views import FlatListView, FlatDetailView, FloorListView, FloorDetailView

urlpatterns = [
    path('flats/', FlatListView.as_view()),
    path('flats/<int:flat_id>/', FlatDetailView.as_view()),
    path('floors/', FloorListView.as_view()),
    path('floors/<int:pk>/', FloorDetailView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
