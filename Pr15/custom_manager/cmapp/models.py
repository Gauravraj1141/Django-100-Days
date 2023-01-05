from django.db import models
from .mymanager import custommanager, proxy_custom_manager


class User(models.Model):
    name = models.CharField(max_length=44)
    age = models.IntegerField()
    marks = models.IntegerField()

# here we give default manager so we can change the name of this default manager
    custom = models.Manager()


class myuser(models.Model):
    name = models.CharField(max_length=44)
    age = models.IntegerField()
    marks = models.IntegerField()

    # here we need to give our default manager name
    objects = models.Manager()

    # here we use custom manager and give some filter in it
    mycustom = custommanager()


class myuser_proxy(myuser):
    pr_manager = proxy_custom_manager()

    class Meta:
        proxy = True
        ordering = ["age"]
