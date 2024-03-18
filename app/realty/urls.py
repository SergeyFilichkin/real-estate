from django.conf.urls.static import static
from django.urls import path

from config import settings
from .domain.building.urls import building_list, building_detail
from .domain.flat.urls import flat_list, flat_detail
from .domain.floor.urls import floor_list, floor_detail
from .domain.project.urls import project_list, project_detail

urlpatterns = [
    flat_list,
    flat_detail,
    floor_list,
    floor_detail,
    building_list,
    building_detail,
    project_list,
    project_detail
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
