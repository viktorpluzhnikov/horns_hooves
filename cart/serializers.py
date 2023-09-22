from rest_framework.serializers import ModelSerializer
from .models import Cart


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartUpdateSerializer(ModelSerializer):

    class Meta:
        model = Cart
        fields = ['product', 'quantity']
