from django.contrib import admin
from .models import *
from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin


@admin.register(LocationData)
class EventAdmin(LeafletGeoAdmin):
    list_display = ('state','district','place','latitude','longitude')

