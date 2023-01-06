from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Trade1(models.Model):
    # here we create onetoone field with user model so we can create user's profile and add some more fields in it
    usname = models.OneToOneField(User, verbose_name=_(
        "tradeuser"), on_delete=models.CASCADE)

    # is user delte his profile that in it so user can't delete his profile until trade1 will delete if it will delte so user will free from here then user will delete
    # usname = models.OneToOneField(User, verbose_name=_(
    #     "tradeuser"), on_delete=models.PROTECT)

    # if we want to set limit to the user only staff user can make a table in trade1 then we can set limit here
    # so if user will in staff then create  here trade1 other wise not
    # so in our users when we add usname then which selected name will show that are in staff
    # usname = models.OneToOneField(
    #     User,  on_delete=models.CASCADE, limit_choices_to={"is_staff": True})
    price = models.IntegerField()
    stockname = models.CharField(max_length=55)


# so here we inherit here trade1 so here relationship will create one to one automatically but if we want to create one to one raltionship with it by our own so we give parentlink = True

class Trade2(Trade1):
    oldtradename = models.OneToOneField(
        Trade1,  on_delete=models.CASCADE, parent_link=True)
    newtradeprice = models.IntegerField()
    nameofnewtrade = models.CharField(max_length=33)
