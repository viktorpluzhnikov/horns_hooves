from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import User, ProductCategory, Product, Basket, CartProduct, Categories


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductCategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BasketSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'


class OrderItemSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CartProduct
        fields = '__all__'


class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
