from rest_framework.viewsets import ModelViewSet
from .serializers import ProductsSerializer
from .models import Product


class ProductCategoryListView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    filterset_fields = ['category']
