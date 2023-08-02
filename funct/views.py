from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import User, ProductCategory, Product, Basket, CartProduct, Categories
from .serializers import UserSerializer, ProductCategorySerializer, ProductSerializer, BasketSerializer, OrderItemSerializer, CategorySerializer
from rest_framework.response import Response



class ProductPagination(LimitOffsetPagination):
    default_limit = 10


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['category', 'price', 'name']
    pagination_class = ProductPagination


class BasketViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
#     permission_classes = [IsAuthenticated]


class OrderView(ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = CartProduct.objects.all()

    @classmethod
    def get_extra_actions(cls):
        return []

    def post(self, request, *args, **kwargs):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


