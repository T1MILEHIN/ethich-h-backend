from django.shortcuts import render
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from account.models import USERS
from .models import paymentStatus
from django.conf import settings

from rest_framework import viewsets
from the_api.models import paymentStatus
from .serializers import USER_REGISTRATION, paymentStatusSerialiizer

# Create your views here.

@api_view(["GET", "POST"])
def usercreation(request):
    if request.method == 'GET':
        # Fetch all users
        users = USERS.objects.all()
        serializer = USER_REGISTRATION(users, many=True)
        for item in serializer.data:
            if item['profile_image']:
                item['profile_image'] = request.build_absolute_uri(item['profile_image'])
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = USER_REGISTRATION(data=request.data)
        if serializer.is_valid():
           user = serializer.save()
            
            # Create PaymentStatus for the new user
           paymentStatus.objects.create(user=user, payment_status=False)
            
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class USERCREATION(ListCreateAPIView):
    queryset =  USERS.objects.all()
    serializer_class = USER_REGISTRATION


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["email"] = user.email
        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class paymentStatusView(viewsets.ModelViewSet):
    queryset = paymentStatus.objects.all()
    serializer_class = paymentStatusSerialiizer