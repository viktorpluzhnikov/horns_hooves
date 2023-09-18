from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializer, CartUpdateSerializer
from .models import Cart
from rest_framework.views import APIView
from products.models import Product
from rest_framework.response import Response
from rest_framework import status


class CartView(APIView):
    permission_classes = [IsAuthenticated]
    """Добавление товара в корзину"""
    def post(self, request):
        cart = Cart(
            product=Product.objects.get(pk=request.data.get("product")),
            quantity=request.data.get("quantity"),
            price=Product.objects.filter(id=request.data.get("product")).first().price,
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
    permission_classes = [IsAuthenticated]
    #queryset = Cart.objects.all()
    serializer_class = CartUpdateSerializer

    def get_queryset(self):
        user = self.request.user.pk
        return Cart.objects.filter(user_id=user)











# class CartDetailView(APIView):
#     permission_classes = [IsAuthenticated]
#     """Получение конкретного продукта"""
#     def get(self, request, pk):
#         cart = Cart.objects.filter(pk=pk, user_id=request.user.id)
#         serializer = CartUpdateSerializer(cart, many=True)
#         return Response(serializer.data)
#
#     """Изменение конкретного товара"""
#     def put(self, request, pk):   #передавать айдишник продукта
#         product = Cart.objects.filter(pk=pk, user_id=request.user.id).update('quantity')
#         serializer = CartSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()                          #сериалайзеры используют только на входе. не использовать в середине кода. использовать лоучше пайдантик модели
#             return Response(serializer.data)            #либо продукт либо рк
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     """Удаление конкретного товара из корзины"""
#     def delete(self, request, pk):
#         cart = Cart.objects.filter(pk=pk, user_id=request.user.id).first()
#         cart.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class CartUpdateView(generics.GenericAPIView,
#                      mixins.DestroyModelMixin,
#                      mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin):
#     permission_classes = [IsAuthenticated]
#     queryset = Cart.objects.all()
#     serializer_class = CartUpdateSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)








# Вот пример реализации `CartView` с использованием generics в Django REST Framework,
# который поддерживает получение, добавление, изменение и удаление товаров в корзине, при этом пользователь может получать только свою корзину.
#
# ```python
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from .models import Cart, CartItem
# from .serializers import CartSerializer, CartItemSerializer
# from .permissions import IsOwner
#
# class CartView(generics.RetrieveAPIView):
# queryset = Cart.objects.all()
# serializer_class = CartSerializer
# permission_classes = [IsAuthenticated, IsOwner]
#
# def get_object(self):
# user = self.request.user
# cart, created = Cart.objects.get_or_create(user=user)
# return cart
#
# class CartItemView(generics.ListCreateAPIView):
# queryset = CartItem.objects.all()
# serializer_class = CartItemSerializer
# permission_classes = [IsAuthenticated, IsOwner]
#
# def get_queryset(self):
# user = self.request.user
# cart = Cart.objects.get(user=user)
# return CartItem.objects.filter(cart=cart)
#
# def perform_create(self, serializer):
# user = self.request.user
# cart = Cart.objects.get(user=user)
# serializer.save(cart=cart)
#
#
# class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
# queryset = CartItem.objects.all()
# serializer_class = CartItemSerializer
# permission_classes = [IsAuthenticated, IsOwner]
# ```
#
# В этом примере есть два класса представлений: `CartView` и `CartItemView`. `CartView` предоставляет пользователю доступ только к своей корзине, а `CartItemView` позволяет пользователю управлять товарами в своей корзине.
#
# Вы также должны создать соответствующие сериализаторы `CartSerializer` и `CartItemSerializer`, а также классы разрешений `IsOwner`, чтобы пользователи могли получать, добавлять, изменять и удалять только свои товары и корзины.
#
# Не забудьте добавить эти представления в URL-маршруты, чтобы можно было получать к ним доступ.
#
# ```python
# from django.urls import path
# from .views import CartView, CartItemView, CartItemDetailView
#
# urlpatterns = [
# path('cart/', CartView.as_view(), name='cart'),
# path('cart/items/', CartItemView.as_view(), name='cart-items'),
# path('cart/items//', CartItemDetailView.as_view(), name='cart-item-detail'),
# ]
# ```
#
# Это простой пример реализации с использованием generics в Django REST Framework для управления товарами в корзине, где пользователь может получать, добавлять, изменять и удалять только свои товары и корзину. Вы можете настроить и дополнить этот пример в соответствии со своими потребностями и логикой приложения.