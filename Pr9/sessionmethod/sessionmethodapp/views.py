from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def setsession(request):
    request.session["Name"] = "Gaurav Rajput"

    return render(request, "ssapp/setsession.html")


def getsession(request):
    if "Name" in request.session:
        sessiondata = request.session["Name"]
        # we use here modified true so when we refrest our page means make any changes in page then session time will increase agian 20 sec
        request.session.modified = True
        return render(request, "ssapp/getsession.html", {"mydata": sessiondata})
    else:
        return HttpResponse("your session has been expired")


def delsession(request):

    # it is delete all the session key data and all
    request.session.flush()
    # we should use this clear_expired because when our session will expire in 10 sec then in our database data will not delete so when we use it then data will clear.
    request.session.clear_expired()

    return render(request, "ssapp/delsession.html")
