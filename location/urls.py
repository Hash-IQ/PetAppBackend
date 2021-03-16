from django.urls import path, include
from rest_framework import routers
from .views import AllLocationViewset, CreateLocationViewset, locationCategoryView, SearchList, SearchDistList
urlpatterns = [
    path('alllocationdata', AllLocationViewset.as_view()),
    path('createlocation', CreateLocationViewset.as_view()),
    path('district', locationCategoryView.as_view()),
    path('searchlocation', SearchList.as_view()),
    path('searchlocationDistrict', SearchDistList.as_view()),
]
