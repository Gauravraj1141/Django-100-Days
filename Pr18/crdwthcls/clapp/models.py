from django.db import models
from django.utils import timezone
# Create your models here.


class User(models.Model):
    UsId = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Phone = models.CharField(max_length=20)
    Date = models.DateTimeField(auto_now=True)
