from django.conf.urls.static import static
from django.urls import path, include

from config import settings

api_v1_urls = [
    path('flats/', include('realty.domain.flat.urls')),
    path('buildings/', include('realty.domain.building.urls')),
    path('floors/', include('realty.domain.floor.urls')),
    path('projects/', include('realty.domain.project.urls'))
]

urlpatterns = [
    path('v1/', include(api_v1_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
