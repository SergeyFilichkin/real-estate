from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from config import settings

from realty.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/flatlist/', FlatListApi.as_view()),
    path('api/flats/<int:flat_id>/', FlatDetailView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
