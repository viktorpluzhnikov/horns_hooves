from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import ProductCategorySerializer
from .models import ProductCategory


class ProductCategoryView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
