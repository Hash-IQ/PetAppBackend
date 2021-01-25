from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
# Create your models here.
class LocationData(models.Model):
    state =models.CharField(max_length=255)
    district =models.CharField(max_length=255)
    place =models.CharField(max_length=255)
    latitude =models.CharField(max_length=500)
    longitude=models.CharField(max_length=500)
    # coordinates = models.PointField(default=Point(0.0,0.0))

    def __str__(self):
        return self.district