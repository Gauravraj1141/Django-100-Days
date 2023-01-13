from django.shortcuts import render, HttpResponse

# here we need to create a view function that show form on the template

from django.contrib.auth.views import LoginView


def home(request):
    return render(request, "registration/home.html")


# here we need to give profile url so we create function here when user login
def profile(request):
    return HttpResponse("hey welcome to your profile")


# change our password

def passwordchange(request):
    return render(request, "registration/password_change_form.html")
