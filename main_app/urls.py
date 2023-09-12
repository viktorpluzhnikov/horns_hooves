"""
URL configuration for main_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from funct.views import UserModelViewSet, ProductCategoryViewSet, ProductViewSet, BasketViewSet, OrderView, CategoryViewSet
from rest_framework.authtoken import views
from product_category.views import ProductCategoryView
from products.views import ProductView

# router = DefaultRouter()
#
# router.register('user', UserModelViewSet)
# router.register('products', ProductCategoryViewSet)
# router.register('product', ProductViewSet)
# router.register('cart', BasketViewSet)
# router.register('order', OrderView)
# router.register('categories', CategoryViewSet)
# router.register('product_category', ProductCategoryView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('products/', ProductCategoryView.as_view()),
    path('product/', ProductView.as_view())
]
