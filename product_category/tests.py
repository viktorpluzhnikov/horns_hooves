# from django.test import TestCase
# from rest_framework.test import APIRequestFactory
# from rest_framework import status
# from product_category.views import ProductCategoryView
#
# class TestCategoryViewSet(TestCase):
#
#     def test_create_guest(self):
#         factory = APIRequestFactory()
#
#         request = factory.post('/category/', {'name': 'test_category'})
#         view = ProductCategoryView.as_view()
#         response = view(request)
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
