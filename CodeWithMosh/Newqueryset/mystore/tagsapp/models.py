
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Lable(models.Model):
    lable_name = models.CharField(max_length=44)


class LabelTag(models.Model):
    title = models.CharField(max_length=444)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    label = models.ForeignKey(Lable , on_delete=models.CASCADE)


