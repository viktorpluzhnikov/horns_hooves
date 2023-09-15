from rest_framework.serializers import ModelSerializer
from .models import Cart
from rest_framework import serializers


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


"""Для обработки запроса на создание или обновление корзины покупок"""
class CartRequestSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)
    price = serializers.DecimalField(max_digits=8, decimal_places=2, default=0)

#     def create(self, validated_data):
#         return validated_data
#
#     def update(self, instance, validated_data):
#         instance['quantity'] = validated_data.get('quantity', instance['quantity'])
#         return instance


class CartResponseSerializer(ModelSerializer):

    class Meta:
        model = Cart
        fields = ['quantity', 'price', 'product']