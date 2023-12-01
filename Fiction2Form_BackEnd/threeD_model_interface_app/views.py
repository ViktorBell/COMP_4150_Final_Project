from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import ThreeDModel, ModelTextureMap, Review, Share, Tag
from .serializers import (ThreeDModelSerializer, ModelTextureMapSerializer,
                          ReviewSerializer, ShareSerializer, TagSerializer)

class ThreeDModelListCreateView(generics.ListCreateAPIView):
    queryset = ThreeDModel.objects.all()
    serializer_class = ThreeDModelSerializer

class ThreeDModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ThreeDModel.objects.all()
    serializer_class = ThreeDModelSerializer

# Similarly, create views for ModelTextureMap, Review, Share, and Tag
