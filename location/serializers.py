from rest_framework import serializers
from  . models import LocationData

class createLocationDataSerializer(serializers.ModelSerializer):
    class Meta :
        model = LocationData
        fields = '__all__'

class getLocationDataSerializer(serializers.ModelSerializer):
    class Meta :
        model = LocationData
        fields = ['district','state','place','latitude','longitude']