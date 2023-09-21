from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from django.contrib.auth.models import User
from cart.views import CartView, CartList, CartDetail
from cart.models import Cart
from product_category.models import ProductCategory
from products.models import Product
import requests
from requests.auth import HTTPBasicAuth


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

    # def test_put_positive(self):
    #     client = APIClient()
    #     client.login(username='admin', password='admin123456')
    #     response = client.put(f'/cart_detail/1/', {'product': self.product, 'quantity': 33, 'price': '333'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     cart = Cart.objects.get(id=id)
    #     self.assertEqual(cart.product, f'{self.product}')
    #     self.assertEqual(cart.quantity, '33')
    #     client.logout()


# class TestPositive(APITestCase):
#     def setUp(self):
#         self.product_category = ProductCategory.objects.create(name='test_category_for_cart')
#         self.product = Product.objects.create(name='test_product', quantity=7, price='50.0', category=self.product_category)
#         self.admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')

    # def test_put_positive(self):
    #     self.client.login(username='admin', password='admin123456')
    #     response = self.client.put(f'/cart_detail/1/', {'product': self.product, 'quantity': 21, 'price': '228'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     cart = Cart.objects.get(id=id)
    #     self.assertEqual(cart.quantity, 21)

    # def test_post_guest(self):
    #     resp = requests.post('http://127.0.0.1:8000/cart/', {'product': self.product, 'quantity': 15, 'price': self.product.price, 'user': self.admin}, auth=HTTPBasicAuth('admin', 'admin123456'))
    #
    #     response = Cart.objects.filter().first()
    #     self.assertEqual(response, {
    #         'product': self.product,
    #         'quantity': 15,
    #         'price': self.product.price
    #     })

    # def test_create_cart(self):
    #     user = User.objects.create(password=123123,
    #                                username="test12",
    #                                is_superuser=True
    #                                )
    #     user.save()
    #     resp = requests.post('http://127.0.0.1:8000/cart/',
    #                          data={
    #                              "quantity": 10,
    #                              "price": 1000,
    #                              "products": 2
    #                          }, auth=HTTPBasicAuth("test12", 123123))
    #     data = resp.json()
    #     response = Cart.objects.filter().first()
    #     self.assertEqual(response, {
    #         ("quantity", 10), ("products", 1), ("user_id", 1)
    #     })