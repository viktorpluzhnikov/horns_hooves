from django.db import models
from products.models import Product
#from user.models import User
from django.contrib.auth.models import User


class Order(models.Model):
    products = models.ManyToManyField(Product, related_name="orders", blank=True)
    quantity = models.IntegerField(default=1)
    created_up = models.DateTimeField(auto_now_add=True)
    delivery_address = models.TextField()
    payment_method = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Заказ пользователя {self.user}'
