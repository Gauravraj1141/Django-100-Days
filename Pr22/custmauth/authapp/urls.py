from django.urls import path, include

# here we import login view logoutview
from django.contrib.auth.views import LoginView, LogoutView

# here we give all urls for authentication view and we override all the views of this authenticationview

from . import views
urlpatterns = [
    # path("login/", LoginView.as_view(template_name="authapp/login.html",
    #      redirect_field_name="/"), name="login"),
    # path("logout/", LogoutView.as_view(template_name="authapp/logout.html"), name="logout"),


    # here we can create our view for these
    path("login/", views.UserLogin.as_view(), name="login"),

    # we create custom logout view
    path("logout/", views.UserLogOut.as_view(), name="logout"),

    # password change url
    path("paswchange/", views.PasswordChange.as_view(), name="paswchange"),

    # password reset url

    path("pswreset/", views.Pswreset.as_view(), name="pswreset"),

    # we need to give one more link for showing when we send email and then redirect on it

    path("pswreset/Psw_reset_send_link/", views.Pswreset_send_link.as_view(),
         name="Psw_reset_send_link"),

    # it is for password rest confirm view here  we can set our password
    path("password_reset_confirm/<uidb64>/<token>/",
         views.Psw_reset.as_view(), name="password_reset_confirm"),




    path("", views.Home.as_view(), name="home"),
    path("customProfile/", views.CustomPF.as_view(), name="customprofile"),
]
