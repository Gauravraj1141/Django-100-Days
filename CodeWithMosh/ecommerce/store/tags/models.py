from django.db import models

# we can create generic foreignkey with the help of content type
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Tag(models.Model):
    label = models.CharField(max_length=444)


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # here we create a generic relationship for any model where we want to create relation with it
    content_type = models.ForeignKey(ContentType,  on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
