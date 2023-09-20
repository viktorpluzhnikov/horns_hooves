# from django.test import TestCase
#
# from .views import CartView
# from product_category.models import ProductCategory
# from products.models import Product
#
#
# # class TestCartViewSet(TestCase):   #не от тест кейса наслед, должен быть сетап
# #
# #     def test_get_list(self):
# #         factory = APIRequestFactory()
# #         request = factory.get('cart_list/')
# #         view = CartList.as_view({'get': 'list'})
# #         response = view(request)
# #         self.assertEquals(response.status_code, status.HTTP_200_OK)
# #
# #     def test_create_guest(self):
# #         factory = APIRequestFactory()
# #
# #         request = factory.post('cart/', {'product': 2, 'quantity': 144}, format='json')
# #         view = CartView.as_view({'post': 'create'})
# #         response = view(request)
# #         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#
#
# class TestCartCreateView(TestCase):
#
#     def setUp(self):
#         category = ProductCategory.objects.create(name="Test Category")
#         category.save()
#         product = Product.objects.create(name="Test Product",
#                                          price="100.5",
#                                          quantity="100",
#                                          category=category)
#         product.save()
#
#     def test_create_cart(self):
#         # user = User.objects.create(password='A1b2c3eQWE',
#         #                            username="TestUsername",
#         #                            is_superuser=True
#         #                            )
#         # user.save()
#         # resp = requests.post('http://127.0.0.1:8000/cart/',
#         #                      data={
#         #                          "quantity": 10,
#         #                          "price": 1000,
#         #                          "products": 2
#         #                      }, auth=HTTPBasicAuth("TestUsername", "A1b2c3eQWE"))
#         # data = resp.json()
#         request = {"quantity": 10,
#                    "price": 1000,
#                    "products": 2}
#         response = CartView.as_view(request)
#         self.assertEqual(response.get("quantity"),10)
#
#     # {
#     #     ("quantity", 10), ("products", 1), ("user_id", 1)
#     # })
#
#     # def tearDown(self):
#     #     ProductCategory.objects.all().delete()
#     #     Product.objects.all().delete()
#     #     User.objects.all().delete()
#     #     Cart.objects.all().delete()
