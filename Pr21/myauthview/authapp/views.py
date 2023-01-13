from django.shortcuts import render, HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# here we need to create a view function that show form on the template
# here we give staff memeber required so only staff member can show this


@staff_member_required
def home(request):
    return render(request, "registration/home.html")


# here we need to give profile url so we create function here when user login
# here we give login required so until user doesn't login until profile will not show
@login_required
def profile(request):
    return render(request, "registration/profile.html")


# change our password

def passwordchange(request):
    return render(request, "registration/password_change_form.html")
