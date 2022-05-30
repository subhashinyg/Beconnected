from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from rest_framework import generics

from rest_framework_simplejwt.tokens import RefreshToken

from user_app.api.serializers import AccountRegistrationSerializer, UserProfileAPISerializer

from rest_framework.views import APIView

from user_app.models import Account



@api_view(['POST',])
def user_registration_view(request):

    if request.method == 'POST':
        serializer = AccountRegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = 'Registration successful'
            data['full_name'] = account.full_name
            data['email'] = account.email
            data['phone'] = account.phone
            
            
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access':str(refresh.access_token),

            }
        else:
            data = serializer.errors
        
        
        return Response(data)

class UserProfileAPI(APIView):
   def get(self, request):
       #user = UserProfileAPISerializer(data=request.data) 
       users=request.Account
       results={"users":users}
       return Response(users)
         
