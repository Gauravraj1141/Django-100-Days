from django.db import models


class mystudents(models.Model):
    stu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=33)
    clsname = models.CharField(max_length=34)
    marks = models.IntegerField()
    address = models.CharField(max_length=44)
