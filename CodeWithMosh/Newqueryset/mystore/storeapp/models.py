from django.db import models

from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=44)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.IntegerField()

