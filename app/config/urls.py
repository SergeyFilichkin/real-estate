from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from config import settings

from realty.views import FlatListView, FloorDetailView, FlatDetailView, FloorListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('api/flats/', FlatListView.as_view()),
    path('api/flats/<int:flat_id>/', FlatDetailView.as_view()),
    path('api/floors/flats/', FloorListView.as_view()),
    path('api/floors/<int:pk>/flats/', FloorDetailView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
