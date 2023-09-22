from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['products', 'quantity', 'created_up', 'delivery_address', 'payment_method', 'user']


class OrderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['delivery_address', 'payment_method']



