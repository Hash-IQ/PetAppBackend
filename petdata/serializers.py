from rest_framework import serializers
from petdata . models import createPet

class createPetSerializer(serializers.ModelSerializer):
    class Meta :
        model = createPet
        fields = '__all__'

class updatePetSerializer(serializers.ModelSerializer):
    class Meta :
        model = createPet
        fields = ['pet_name','amount','description','transportation','age']
         
         