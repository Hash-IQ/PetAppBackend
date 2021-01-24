from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    # id                  = models.CharField(primary_key=True,max_length=30)
    mobile              = models.CharField(max_length=30, blank=True)
            
    def __str__(self):
        return self.username