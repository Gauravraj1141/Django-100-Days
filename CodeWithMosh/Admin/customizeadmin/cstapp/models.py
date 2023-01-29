from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=444)
    price = models.IntegerField()
    collection = models.ForeignKey("Collection", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    #  here we annotate it like as string means it retuns string so we give here -> str  here

    def __str__(self) -> str:
        return self.name


class Collection(models.Model):
    title = models.CharField(max_length=333)

    def __str__(self) -> str:
        return self.title
