from django.db import models
from account.models import User
from django.core.exceptions import ValidationError
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
# Create your models here.


class createPet(models.Model):
    owner = models.ForeignKey(
        User, related_name="pets", null=True, on_delete=models.CASCADE)
    owner_name=models.CharField(max_length=255)
    owner_image=models.CharField(max_length=255)
    owner_phone=models.CharField(max_length=255)
    pet_name = models.CharField(max_length=255)
    pet_category = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    age = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=500)
    latitude =models.CharField(max_length=500)
    longitude=models.CharField(max_length=500)
    coordinates = models.PointField(default=Point(0.0,0.0))
    transportation = models.BooleanField(default=False)
    saled = models.BooleanField(null=True, blank=True)
    photo1 = models.FileField(upload_to='media/dp',blank=True)  
    photo2 = models.FileField(upload_to='media/dp',blank=True)  
    photo3 = models.FileField(upload_to='media/dp',blank=True)  
    photo4 = models.FileField(upload_to='media/dp',blank=True)  
    video  = models.FileField(upload_to='videos/',blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
 

    def __str__(self):
        return self.pet_name
