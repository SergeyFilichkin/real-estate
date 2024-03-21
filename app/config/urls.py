from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('realty/', include('realty.urls')),
]
