from django.urls import path
from .views import ProductCategoryListView

urlpatterns = [
    path('product/', ProductCategoryListView.as_view({'get': 'list'}))
]