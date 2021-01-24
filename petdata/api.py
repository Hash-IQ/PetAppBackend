import datetime
from functools import reduce
from django.core import serializers
from django.db.models import Q
from rest_framework import generics, permissions, status, viewsets
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from petdata.models import createPet
from .serializers import createPetSerializer, updatePetSerializer

from PettApp.authentication import FirebaseAuthentication
from django.http import Http404, HttpResponse
from django.contrib.gis.geos import Point
from rest_framework.views  import APIView
from django.contrib.gis.measure import D, Distance


#petdata creation
class CreatePetViewset(generics.ListCreateAPIView):

    authentication_classes = [FirebaseAuthentication]

    serializer_class = createPetSerializer
    
    def perform_create(self, serializer):
        latitude = float(serializer.initial_data['latitude'])
        longitude = float(serializer.initial_data['longitude'])
        user_location = Point(x=longitude, y=latitude, srid=4326)
        serializer.save(owner=self.request.user,coordinates=user_location)


#user petdata view
class UserPetViewset(generics.ListAPIView):
    authentication_classes = [FirebaseAuthentication]
    serializer_class = createPetSerializer

    def get_queryset(self):
        user = self.request.user
        return createPet.objects.filter(owner=user)


#all petdata view
class AllPetViewset(generics.ListAPIView):
    authentication_classes = [FirebaseAuthentication]
    serializer_class = createPetSerializer

    def get_queryset(self):

        return createPet.objects.all()


# petdata view
class petCategoryView(generics.ListAPIView):
    authentication_classes = [FirebaseAuthentication]
    serializer_class = createPetSerializer

    def get_queryset(self):
        latitude = self.request.query_params.get('latitude', )
        longitude = self.request.query_params.get('longitude', )
        _x=float(latitude)
        _y=float(longitude)
        location = Point(_x,_y,srid=4326)
        category = self.request.query_params.get('category', )
        return createPet.objects.filter(pet_category=category,coordinates__distance_lte=(location, D(km=100)))

    # def post(self, request):
    #     category = request.POST.get("category")
    #     return HttpResponse(createPet.objects.filter(pet_caegory=category))
class locationBasedView(generics.ListAPIView):
    authentication_classes = [FirebaseAuthentication]
    serializer_class = createPetSerializer

    def get_queryset(self):
        latitude = self.request.query_params.get('latitude', )
        print(latitude)
        longitude = self.request.query_params.get('longitude', )
        print(type(longitude))
        
        _x=float(latitude)
        _y=float(longitude)
        location = Point(_x,_y,srid=4326)
        print(location)

        return createPet.objects.filter(coordinates__distance_lte=(location, D(km=100)))



class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    
    """
    authentication_classes = [FirebaseAuthentication]  
    serializer_class = createPetSerializer
    def get_object(self, pk):
        try:
            return createPet.objects.get(id=pk)
        except createPet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        message = { 
                "message": "Successfully Deleted ",
                "status": str(status.HTTP_204_NO_CONTENT)
                }
        return Response(message,status.HTTP_204_NO_CONTENT)
      

    def post(self, request, pk, format=None,many=False):
        saled = self.get_object(pk)
        serializer = updatePetSerializer(saled, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
class SearchList(generics.ListAPIView):
    authentication_classes = [FirebaseAuthentication]  
    serializer_class = createPetSerializer

    def get_queryset(self):
        latitude = self.request.query_params.get('latitude', )
        print(latitude)
        longitude = self.request.query_params.get('longitude', )
        print(type(longitude))
        
        _x=float(latitude)
        _y=float(longitude)
        location = Point(_x,_y,srid=4326)
        print(location)
        category = self.request.query_params.get('petName', )
        return createPet.objects.filter(pet_name__contains=category,coordinates__distance_lte=(location, D(km=100)))
    