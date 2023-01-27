from django.db import models


class OwnerDetails(models.Model):
    name = models.CharField(max_length=444)
    email = models.EmailField()
    phone = models.CharField(max_length=44)
    address = models.CharField(max_length=455)
    property = models.ManyToManyField('PropertyOwner')


class PropertyOwner(models.Model):
    name = models.CharField(max_length=444)
    price = models.IntegerField()

    def __str__(self):
        return self.id
