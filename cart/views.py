from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializer, CartUpdateSerializer
from .models import Cart
from rest_framework.views import APIView
from products.models import Product
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


class CartView(APIView):
    permission_classes = [IsAuthenticated]
    """Добавление товара в корзину"""

    @swagger_auto_schema(
        operation_summary="Добавление товара в корзину",
        request_body=CartUpdateSerializer,
        responses={
            201: CartSerializer,
            400: "Неправильный ввод данных",
            500: "Серверная ошибка",
        },
    )
    def post(self, request):
        cart = Cart(
            product=Product.objects.get(pk=request.data.get("product")),
            quantity=request.data.get("quantity"),
            price=Product.objects.filter(id=request.data.get("product")).first().price * request.data.get("quantity"),
            user_id=request.user.id
        )
        cart.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # """Просмотр всех товаров в корзине"""
    # def get(self, request):
    #     cart = Cart.objects.filter(user_id=request.user.id).all()
    #     serializer = CartSerializer(cart, many=True)
    #     return Response(serializer.data)
    # """Удаление всех товаров в корзине"""
    # def delete(self, request):
    #     cart = Cart.objects.filter(user_id=request.user.id).all()
    #     cart.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #
    # def sum(self):
    #     return self.cart.quantity * self.cart.product.price


class CartList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer
    """GET - Корзина авторизованного пользователя"""
    def get_queryset(self):
        user = self.request.user.pk
        return Cart.objects.filter(user_id=user)


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    """PUT, DELETE"""
    http_method_names = ['put', 'delete']
    permission_classes = [IsAuthenticated]
    serializer_class = CartUpdateSerializer

    def get_queryset(self):
        user = self.request.user.pk
        return Cart.objects.filter(user_id=user)
