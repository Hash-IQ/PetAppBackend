from account.models import User
from rest_framework import authentication
from rest_framework import exceptions
from firebase_admin import auth
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        
        token = request.headers.get('Authorization')
        if not token:
            message = { 
                "message": "You don't have enough permission please provide a token",
                "status": status.HTTP_403_FORBIDDEN
                }
            raise AuthenticationFailed(message)

        try:
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token["uid"]
        except:
            message = { 
                "message": "You don't have enough permission please provide a valid tocken",
                "status": status.HTTP_403_FORBIDDEN
                }
            raise AuthenticationFailed(message)

        try:
            user = User.objects.get(username=uid)
        except User.DoesNotExist:
            message = { 
                "message": "Coudn't find a valid user in our database",
                "status": status.HTTP_403_FORBIDDEN
                }
            raise AuthenticationFailed(message)

        return (user, None)
        
        # # # Test Only ##
        # user = User.objects.get(username='BkVTy9o8O3Te8CVCkHNvVHXprDn2')
        # return (user, None)