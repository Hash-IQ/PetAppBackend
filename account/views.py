from django.shortcuts import render
from account.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from firebase_admin import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from account.serializers import profileSerilizer
from PettApp.authentication import FirebaseAuthentication
# Create your views here.


class UpdateNameView(APIView):
    def post(self, request):
        uid = request.headers.get('Authorization')
        decoded_token = auth.verify_id_token(uid)
        uid = decoded_token['uid']
        print(uid)
        # Check if User is valid or not #
        try:
            firebase_user = auth.get_user(uid)
        except:
            message = {
                "message": "User Not Valid",
                "status": str(status.HTTP_403_FORBIDDEN)
            }
            raise AuthenticationFailed(message)

        # Trying to fetch a User with Firebase uid exist's , if not create a new user and fetch user's display name #
        try:
            user = User.objects.get(username=uid)
            user.first_name = firebase_user.display_name
            user.save()
        except:
            user = User(username=uid,
                        first_name=firebase_user.display_name,
                        is_active=True)
            user.save()
        message = {
            "message": "Successfully Updated first_name",
            "status": str(status.HTTP_201_CREATED),
            "phone": user.mobile
        }
        return Response(message, status.HTTP_201_CREATED)


class mobileSave(APIView):
    authentication_classes = [FirebaseAuthentication]
    serializer_class = profileSerilizer

    def post(self, request):
        user = self.request.user
        mobile = request.POST.get('mobile')
        print(mobile)
        user.mobile = mobile
        user.save()
        message = {
            "message": "Successfully Added PhoneD",
            "status": str(status.HTTP_201_CREATED)
        }
        return Response(message, status.HTTP_201_CREATED)
