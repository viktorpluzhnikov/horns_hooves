from rest_framework import generics
from .serializers import ProductsSerializer
from .models import Product


class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    filterset_fields = ['category']

    def get_queryset(self):
        queryset = Product.objects.all()
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)

        return queryset

#http://127.0.0.1:8000/products/?min_price=10&max_price=50
