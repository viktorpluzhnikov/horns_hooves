from django.urls import path
from .views import OrderView, OrderDetailView

urlpatterns = [
    path('order/', OrderView.as_view()),
    path('order_detail/', OrderDetailView.as_view())
]