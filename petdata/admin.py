from django.contrib import admin
from .models import *
from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin


@admin.register(createPet)
class EventAdmin(LeafletGeoAdmin):
    list_display = ('pet_name','pet_category','location','coordinates')

