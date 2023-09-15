from django.db import models
#from products.models import Product


class ProductCategory(models.Model):
    name = models.CharField(max_length=32, unique=True)
    #product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'