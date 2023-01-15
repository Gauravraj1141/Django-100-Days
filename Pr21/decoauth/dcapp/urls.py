from django.urls import path, include
from . import views

# we can give this type of urls in any urls for any views
# we can add here also login required in these urls
from django.contrib.auth.decorators import login_required
# give a staff member required for this about page only staff memebers can access it
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    # here we give login_required in this profile view so without login it will not open it redirect to the login page
    path('profile/', login_required(views.Profile.as_view()), name="profile"),

    path("about/", staff_member_required(views.Aboutpage.as_view()), name="about"),

    path("mypro", views.Myproperty.as_view(), name="mypro")

]
