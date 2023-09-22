import dadata
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import OrderSerializer, OrderPostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from cart.models import Cart
from .models import Order

from dadata import Dadata

token = "17bb15eedc972f4256842981132c365bc811966d"
secret = "a884dbb8cf666fd58ffd2c50f177b240e858a661"
dadata = Dadata(token, secret)


class OrderView(APIView):
    permission_classes = [IsAuthenticated]
    """Оформление заказа"""

    @swagger_auto_schema(
        operation_summary="Оформление заказа",
        request_body=OrderPostSerializer,
        responses={
            201:  OrderSerializer,
            400: "Неправильный ввод данных",
            500: "Серверная ошибка",
        },
    )
    def post(self, request):
        cart = Cart.objects.filter(user_id=request.user.id).all()
        if len(cart) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        order = Order(
            delivery_address=request.data.get("delivery_address"),
            payment_method=request.data.get("payment_method"),
            user_id=request.user.id
        )
        order.delivery_address = dadata.clean(name="address", source=order.delivery_address)
        order.delivery_address = order.delivery_address['result']
        order.save()
        for item in cart:
            order.products.add(item.product)
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