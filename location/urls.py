
from django.urls import path,include
from rest_framework import routers
from .views  import AllLocationViewset,CreateLocationViewset
urlpatterns = [
    path('alllocationdata',AllLocationViewset.as_view()),
    path('createlocation',CreateLocationViewset.as_view()),
  

]
