from django.contrib import admin
from .views import Flat
from .models import Floor

admin.site.register(Flat)
admin.site.register(Floor)
