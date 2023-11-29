from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomUserSerializer

# View that facilitates the registration of new users
@api_view(['POST'])
def register_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
