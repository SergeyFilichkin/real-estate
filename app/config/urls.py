from django.contrib import admin
from django.urls import path
from django.urls import path
from realty.views import FlatListCreateAPIView, FlatRetrieveUpdateDestroyAPIView
from drf_spectacular.views import SpectacularAPIView,  SpectacularSwaggerView


urlpatterns = [
    path('admin', admin.site.urls),
    path('flats/', FlatListCreateAPIView.as_view(), name='flat-list-create'),
    path('flats/<int:pk>/', FlatRetrieveUpdateDestroyAPIView.as_view(), name='flat-retrieve-update-destroy'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
