from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return f'{self.name}'