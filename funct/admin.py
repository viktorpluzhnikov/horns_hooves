from django.contrib import admin
from .models import Product, ProductCategory, Basket, Categories, CartProduct


admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(Categories)
admin.site.register(CartProduct)
