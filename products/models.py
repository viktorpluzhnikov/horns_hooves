from django.db import models
from product_category.models import ProductCategory


class Product(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category}'