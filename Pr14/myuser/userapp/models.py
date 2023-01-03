from django.db import models

# Create your models here.


class students(models.Model):
    Name = models.CharField(max_length=33)
    Email = models.EmailField(max_length=254)
    Phone = models.CharField(max_length=33)
    roll = models.CharField(max_length=33)
    Address = models.CharField(max_length=200)
