from django.urls import path
from .views import ProductCategoryView, ProductCategoryDetailView


urlpatterns = [
    path('products/', ProductCategoryView.as_view()),
    path('products/<int:pk>/', ProductCategoryDetailView.as_view()),
]