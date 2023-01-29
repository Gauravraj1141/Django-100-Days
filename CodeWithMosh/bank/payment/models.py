from django.db import models

import uuid


class Users(models.Model):
    user_id = models.BigAutoField(
        primary_key=True)
    user_name = models.CharField(max_length=44)
    upi_id = models.CharField(max_length=11, unique=True)
    account_balance = models.PositiveBigIntegerField()

    def __str__(self):
        return self.user_name


# class Recharge(models.Model):
#     recharge_id = models.AutoField(
#         primary_key=True, default=uuid.uuid1, editable=False)
#     sender_upi_id = models.CharField(max_length=11)
#     reciever_upi_id = models.CharField(max_length=11)
#     amount = models.IntegerField()
