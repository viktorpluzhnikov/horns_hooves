from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductCategorySerializer
from .models import ProductCategory
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class ProductCategoryView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductCategoryDetailView(APIView):
    permission_classes = [IsAuthenticated]
    """Вывод одной категории """
    def get(self, request, pk):
        products = ProductCategory.objects.filter(pk=pk).first()
        serializer = ProductCategorySerializer(products)
        return Response(serializer.data)




# class ProductCategoryDetailView(generics.ListAPIView):
#     serializer_class = ProductCategorySerializer
#     """Вывод всех категорий """
#     def get_queryset(self, pk):
#         product_category = ProductCategory.objects.filter(pk=pk)
#         return product_category


# class ProductCategoryDetailView(APIView):
#     """Конкретная категория"""
#     def get(self, pk):
#         prod_cat = ProductCategory.objects.get(id=pk)
#         serializer = ProductCategorySerializer(prod_cat)
#         return Response(serializer.data)
