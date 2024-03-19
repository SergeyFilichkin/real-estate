from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from realty.views import  FlatViewSet
from  drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView



router = DefaultRouter()
router.register(r'flats', FlatViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flat', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
