from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    birthday = models.DateField(max_length=8)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class ProductCategory(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField()

    def __str__(self):
        return f'Категория: {self.name} '


class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'


#модель на категории получаем все товары по категории
class Categories(models.Model):
    name_category = models.ManyToManyField(ProductCategory)
    name_product = models.ManyToManyField(Product)


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user} | Продукт: {self.product.name}'


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    # def get_total_item_price(self):
    #     return self.quantity*self.product.price
    #
    # def get_final_price(self):
    #     return self.get_total_item_price()


# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
#     start_date = models.DateTimeField(auto_now=True)
#     ordered_date = models.DateTimeField()
#     ordered = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.user

    # def get_total(self):
    #     total = 0
    #     for order_item in self.product.all():
    #         total += order_item.get_final_price()
    #     return total
