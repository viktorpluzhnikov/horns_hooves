# from user.models import User
from django.contrib.auth.models import User
from django.db import models
from products.models import Product


class Cart(models.Model):
    product = models.ForeignKey(Product, related_name='cart', blank=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Корзина пользователя {self.user}'

    # class Meta:
    #     app_label = 'cart'

    # def sum(self):
    #     return self.quantity * self.product.price

    # def total_quantity(self):
    #     carts = Cart.objects.filter(user=self.user)
    #     return sum(cart.quantity for cart in carts)
    #
    # def total_sum(self):
    #     carts = Cart.objects.filter(user=self.user)
    #     return sum(cart.sum() for cart in carts)
