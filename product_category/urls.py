from django.urls import path
from .views import ProductCategoryView, ProductCategoryDetailView


urlpatterns = [
    path('categories/', ProductCategoryView.as_view()),
    path('categories/<int:pk>/', ProductCategoryDetailView.as_view())
]