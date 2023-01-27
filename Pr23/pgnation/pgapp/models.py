from django.db import models


class Blogs(models.Model):
    blg_id = models.AutoField(primary_key=True)
    blg_name = models.CharField(max_length=100)
    blg_status = models.BooleanField()
