from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from django.contrib.auth.models import User
from cart.views import CartView, CartList, CartDetail
from cart.models import Cart
from product_category.models import ProductCategory
from products.models import Product


class TestCategoryViewSet(TestCase):
    def setUp(self) -> None:
        self.product_category = ProductCategory.objects.create(name='test_category_for_cart')
        self.product = Product.objects.create(name='test_product', quantity=7, price='50.0', category=self.product_category)
        self.admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')

    def test_create_guest(self):
        client = APIClient()
        response = client.post('/cart/', {'product': self.product, 'quantity': 15, 'price': self.product.price, 'user': self.admin})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_guest(self):
        client = APIClient()
        response = client.put(f'/cart_detail/1/', {'product': self.product, 'quantity': 20, 'price': '228'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_guest(self):
        client = APIClient()
        response = client.delete('/cart_detail/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
