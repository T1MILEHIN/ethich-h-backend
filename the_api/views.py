from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from account.models import USERS
from .serializers import USER_REGISTRATION

# Create your views here.

@api_view(["GET", "POST"])
def usercreation(request):
    if request.method == 'GET':
        # Fetch all users
        users = USERS.objects.all()
        serializer = USER_REGISTRATION(users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # Create a new user
        serializer = USER_REGISTRATION(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    


class USERCREATION(ListCreateAPIView):
    queryset =  USERS.objects.all()
    serializer_class = USER_REGISTRATION

