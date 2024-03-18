from django.conf.urls.static import static
from django.urls import path, include

from config import settings

from .domain.building.urls import urlpatterns as building_urls
from .domain.flat.urls import urlpatterns as flat_urls
from .domain.floor.urls import urlpatterns as floor_urls
from .domain.project.urls import urlpatterns as project_urls

urlpatterns = [
    path('v1/', include(building_urls)),
    path('v1/', include(flat_urls)),
    path('v1/', include(floor_urls)),
    path('v1/', include(project_urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
