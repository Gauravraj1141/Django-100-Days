from django.shortcuts import render
from .models import Users
from django.db import transaction

from django.contrib import messages


# when we  give wrong upi id then our balance will cut but if we use this transation.atomic then our balance will roll back means when any error will occur then it will not execute our database query
@transaction.atomic
def Recharge(request):
    if request.method == "POST":
        sender_id = request.POST["sender"]
        receiver_id = request.POST["receiver"]
        amount = request.POST["amount"]

    #    sender a/c updation
        try:
            sender_ac_bal = Users.objects.get(upi_id=sender_id).account_balance

            sender_rest_ac_bal = sender_ac_bal - int(amount)

            sender_ac_update = Users.objects.filter(
                upi_id=sender_id).update(account_balance=sender_rest_ac_bal)

            #    receiver a/c updation

            receiver_ac_bal = Users.objects.get(
                upi_id=receiver_id).account_balance
            reciver_rest_ac_bal = receiver_ac_bal + int(amount)
            receiver_ac_update = Users.objects.filter(
                upi_id=receiver_id).update(account_balance=reciver_rest_ac_bal)

            messages.success(request, "Transaction Completed Successfully")

        except Exception as e:
            messages.success(request, e)

    return render(request, "recharge/home.html")
