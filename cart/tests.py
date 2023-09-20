from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory # фабрика для создания запросов
from .views import CartView, CartList, CartDetail
from .models import Cart
from product_category.models import ProductCategory
#from django.contrib.auth.models import User


class TestCartViewSet(TestCase):   #не от тест кейса наслед, должен быть сетап

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('cart_list/')
        view = CartList.as_view({'get': 'list'})
        response = view(request)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()

        request = factory.post('cart/', {'product': 2, 'quantity': 144}, format='json')
        view = CartView.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# class TestCartCreateView(APITestCase):
#
#     def setUp(self):
#         category = ProductCategory.objects.
