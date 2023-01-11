from django.db import models
from django.urls import reverse


class Locker(models.Model):
    Username = models.CharField(max_length=33)
    Email = models.EmailField()
    Password = models.CharField(max_length=44)

    def get_absolute_url(self):
        return reverse("thankscreate", kwargs={"pk": self.pk})
