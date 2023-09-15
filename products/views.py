import django_filters.rest_framework
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from product_category.models import ProductCategory
from .serializers import ProductsSerializer
from .models import Product
from rest_framework import generics


class ProductCategoryListView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    filterset_fields = ['category']
