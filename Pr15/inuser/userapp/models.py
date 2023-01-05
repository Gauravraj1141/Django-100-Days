from django.db import models

# model inheritence so we inherit the model in other model then table will created and realtion of these will one to one realtionship


class father(models.Model):
    name = models.CharField(max_length=33)
    profession = models.CharField(max_length=44)


class daughter(father):
    age = models.IntegerField()


class son(father):
    age = models.IntegerField()


# here we use proxy model

class User(models.Model):
    name = models.CharField(max_length=44)
    age = models.IntegerField()


# we created proxy model of this User model and these two model table will create only one because it will change the behaviour or this user model only
# and we can't give any field in this proxy model  because it is use only for behaviour
class userproxy(User):

    class Meta:
        proxy = True
        ordering = ["name"]
