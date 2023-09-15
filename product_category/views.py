from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductCategorySerializer
from .models import ProductCategory
from rest_framework.permissions import IsAuthenticated


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
