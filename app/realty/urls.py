from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView
from drf_spectacular.views import SpectacularAPIView
from realty.views import FlatListAPIView
from realty.views import FlatDetailAPIView


urlpatterns = [
    path('admin-panel', admin.site.urls),
    path('flats/', FlatListAPIView.as_view(), name='flat-list-create'),
    path('flats/<int:pk>/', FlatDetailAPIView.as_view(), name='flat-retrieve-update-destroy'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
