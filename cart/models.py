from django.db import models
from products.models import Product
from user.models import User


class Cart(models.Model):
        product = models.ForeignKey(Product, related_name='cart', on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField(default=0)
        price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
        user = models.ForeignKey(User, on_delete=models.CASCADE)



