from django.shortcuts import render, HttpResponse
from . import signals
# Create your views here.


def home(request):
    # here we give this signal when our home will call then this signal will send and we can perform any task
    signals.notification.send(
        sender=None, request=request, user=["Gaurav", "rajput"])
    return HttpResponse("hey it is for testing of our custom signals ")
