from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=33)
    clsname = models.CharField(max_length=44)
    section = models.CharField(max_length=22)
    marks = models.IntegerField()
