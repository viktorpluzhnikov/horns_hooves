from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializer
from .permissions import IsOwner
from .models import Cart



# class CartView(generics.ListCreateAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#
#
# class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer


class CartView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cart.obkects.all()
    serializer_class = CartSerializer
