from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import ProductCategory


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'



