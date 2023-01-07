from django.db import models

from django.contrib.auth.models import User


# here we create many to many relationship with User in this song table

class MusicPlayer(models.Model):
    Song_id = models.AutoField(primary_key=True)
    Song_name = models.CharField(max_length=44)
    Song_duration = models.IntegerField()
    Singers_name = models.ManyToManyField(User)

    # here we need to create a function that show us names of singers name
    def sing_by(self):
        Names_of_singers = ",".join(
            [str(singer) for singer in self.Singers_name.all()])

        return Names_of_singers
