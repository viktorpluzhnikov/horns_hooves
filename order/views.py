from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from cart.models import Cart
from .models import Order


class OrderView(APIView):
    permission_classes = [IsAuthenticated]
    """Оформление заказа"""

    @swagger_auto_schema(
        operation_summary="Оформление заказа",
        request_body=OrderSerializer,
        responses={
            201:  OrderSerializer,
            400: "Неправильный ввод данных",
            500: "Серверная ошибка",
        },
    )
    def post(self, request):
        cart = Cart.objects.filter(user_id=request.user.id).all()
        # if cart in None:
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        order = Order(
            delivery_address=request.data.get("delivery_address"),
            payment_method=request.data.get("payment_method"),
            user_id=request.user.id
        )
        order.save()
        for item in cart:
            order.products.add(item.product)
            #order.quantity.append(item.quantity)
        order.save()
        cart.delete()
        serializer = OrderSerializer(order)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderDetailView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user.pk
        return Order.objects.filter(user_id=user)