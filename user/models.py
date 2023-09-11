from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    birthday = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
