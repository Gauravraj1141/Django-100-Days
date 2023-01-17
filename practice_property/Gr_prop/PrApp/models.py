from django.db import models


class State(models.Model):
    st_id = models.AutoField(primary_key=True)
    stname = models.CharField(max_length=100)

    def __str__(self):
        return self.stname


class City(models.Model):
    ct_id = models.AutoField(primary_key=True)
    ctname = models.CharField(max_length=33)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.ctname


class PropertyDetail(models.Model):
    Pr_id = models.AutoField(primary_key=True)
    Property_name = models.CharField(max_length=100)
    Property_address = models.CharField(max_length=200)
    City_name = models.ForeignKey(City, on_delete=models.CASCADE)
