from django.db import models

# here we create three fields and in three feilds some attribute names are same so we create a abstract base class where we can inherit some field which are common in these table
# here we show how to create abstract base class it is not create a table in database


class Basefields(models.Model):
    name = models.CharField(max_length=70)
    Address = models.CharField(max_length=200)
    Phone = models.CharField(max_length=30)
    Salary = models.IntegerField()

    class Meta:
        abstract = True

# it is a subclass of basefields and all the basefields's field will inherit in it


class Students(Basefields):
    Salary = None
    Clsname = models.CharField(max_length=50)
    roll = models.IntegerField()


class Teacher(Basefields):
    subject = models.CharField(max_length=44)


# so here all fields will inherit in it so we don't need to write any field name here
class Peon(Basefields):
    pass
