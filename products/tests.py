from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status
from django.contrib.auth.models import User
from products.models import Product
from products.views import ProductCategoryListView
from product_category.models import ProductCategory


class TestProductViewSet(TestCase):

    def setUp(self) -> None:
        self.product_category = ProductCategory.objects.create(name='test_category_for_cart')
        self.product = Product.objects.create(name='test_product', quantity=7, price='50.0', category=self.product_category)
        self.admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')

    def test_get_guest(self):
        factory = APIRequestFactory()
        request = factory.get('/product/')
        force_authenticate(request, self.admin)
        view = ProductCategoryListView.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
