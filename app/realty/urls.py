from django.conf.urls.static import static
from django.urls import path, include

from config import settings

flats_api_v1_urls = [path('', include('realty.domain.flat.urls'))]
buildings_api_v1_urls = [path('', include('realty.domain.building.urls'))]
floors_api_v1_urls = [path('', include('realty.domain.floor.urls'))]
projects_api_v1_urls = [path('', include('realty.domain.project.urls'))]

urlpatterns = [
    path('v1/', include(buildings_api_v1_urls)),
    path('v1/', include(flats_api_v1_urls)),
    path('v1/', include(floors_api_v1_urls)),
    path('v1/', include(projects_api_v1_urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
