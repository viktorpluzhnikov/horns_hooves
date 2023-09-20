from rest_framework.viewsets import ModelViewSet
from .serializers import ProductsSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated


class ProductCategoryListView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    filterset_fields = ['price', 'category']
