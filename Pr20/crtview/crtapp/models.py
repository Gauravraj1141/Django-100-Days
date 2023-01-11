from django.db import models
# here we need to import reverse
from django.urls import reverse


class ZoneSchools(models.Model):
    name = models.CharField(max_length=33)
    address = models.CharField(max_length=55)
    Contact_no = models.CharField(max_length=33)

  # we can give redirect url here also when form will submit then it redirect where so we give here

    def get_absolute_url(self):
        # in this kwargs we can give id of that field which we add  and we give here pattern name for redirect
        return reverse("Mydata", kwargs={"pk": self.pk})
