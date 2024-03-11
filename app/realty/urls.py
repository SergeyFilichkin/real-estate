from django.conf.urls.static import static
from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from config import settings
from .views import FlatListView, FlatDetailView, FloorListView, FloorDetailView

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('flats/', FlatListView.as_view()),
    path('flats/<int:flat_id>/', FlatDetailView.as_view()),
    path('floors/', FloorListView.as_view()),
    path('floors/<int:pk>/', FloorDetailView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
