from django.db import models

# in our custommanager we give filter and order by also so we use it when we use some common filter again and again so we need to use it when dry (don't repeat yourself)limit cross
from django.db.models import Q


class custommanager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(marks__lt=400).order_by("name")


# we make this manager for our proxy model
class proxy_custom_manager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(Q(marks__gt=380) & Q(marks__lt=500))
