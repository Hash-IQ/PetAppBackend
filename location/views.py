import datetime
from functools import reduce
from django.core import serializers
from django.db.models import Q
from rest_framework import generics, permissions, status, viewsets
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from .models import LocationData
from .serializers import createLocationDataSerializer

from PettApp.authentication import FirebaseAuthentication
from django.http import Http404, HttpResponse
from django.contrib.gis.geos import Point
from rest_framework.views  import APIView
from django.contrib.gis.measure import D, Distance

# Create your views here.
class CreateLocationViewset(generics.ListCreateAPIView):

    # authentication_classes = [FirebaseAuthentication]

    serializer_class = createLocationDataSerializer
    
    def perform_create(self, serializer):
        latitude = float(serializer.initial_data['latitude'])
        longitude = float(serializer.initial_data['longitude'])
        user_location = Point(x=longitude, y=latitude, srid=4326)
        serializer.save(coordinates=user_location)


class AllLocationViewset(generics.ListAPIView):
    authentication_classes = [FirebaseAuthentication]
    serializer_class = createLocationDataSerializer

    def get_queryset(self):

        return LocationData.objects.all()