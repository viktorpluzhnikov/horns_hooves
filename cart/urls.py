from django.urls import path
from .views import CartView, CartList, CartDetail


urlpatterns = [
    path("cart/", CartView.as_view()),
    path("cart_list/", CartList.as_view()),
    path("cart_detail/<int:pk>/", CartDetail.as_view())
]