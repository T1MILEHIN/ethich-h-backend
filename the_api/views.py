from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from account.models import USERS
from .serializers import USER_REGISTRATION

# Create your views here.

@api_view(["GET", "POST"])
def usercreation(request):
    user = USERS.objects.all()
    serializer = USER_REGISTRATION(user, many=True)
    if request.method == 'POST':
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    return Response(serializer.data)

