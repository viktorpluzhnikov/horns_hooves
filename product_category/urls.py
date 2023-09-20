from django.urls import path
from .views import ProductCategoryView, ProductCategoryDetailView, CategoryPost


urlpatterns = [
    path('categories/', ProductCategoryView.as_view()),
    path('categories/<int:pk>/', ProductCategoryDetailView.as_view()),
    path('category_post/', CategoryPost.as_view({'post': 'list'}))
]