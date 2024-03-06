from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from config import settings
from realty.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/flatlist/', AllFlatsApi.as_view()),
    path('api/flatlist/<int:flat_id>/', FlatApi.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)