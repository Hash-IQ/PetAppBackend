from django.urls import path,include
from rest_framework import routers
from . api import AllPetViewset,CreatePetViewset,UserPetViewset,petCategoryView,locationBasedView,SnippetDetail,SearchList  


urlpatterns = [
    path('allpetdata',AllPetViewset.as_view()),
    path('user_pet',UserPetViewset.as_view()),
    path('create_pet',CreatePetViewset.as_view()),
    path('category_pet',petCategoryView.as_view()),
    path('location_pet',locationBasedView.as_view()),
     path('search_pet',SearchList.as_view()),
    path('all_pet/<int:pk>',SnippetDetail.as_view()),
    #  path('update_pet',SaledUpdateView.as_view()),

]
