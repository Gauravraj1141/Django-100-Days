from django.db import models

# Create your models here.


class students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)
    clname = models.CharField(max_length=55)
    marks = models.IntegerField()
