from django.shortcuts import render

from django.views.generic import TemplateView


# here we import all these operations of authentication view
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView

from django.contrib import messages
# login view


class UserLogin(LoginView):
    template_name = "authapp/login.html"
    # here we can give extra context in it for showing in login page
    extra_context = {"context": "Please login for access the profile "}

    # we can give here also extra data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra_data'] = 'This is some extra data to display'
        return context

    # we can send message to the next url where we can redirect it after login
    def form_valid(self, form):
        authenticated_user = form.get_user()
        messages.success(
            self.request, f'Welcome {authenticated_user.username}')
        return super().form_valid(form)

    # if creadentials is invalid
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid login credentials')
        return super().form_invalid(form)


# logout custom view

class UserLogOut(LogoutView):
    # here we give login url when we logout then it will redirect us on login page
    next_page = "login"

    # so here we don't need to give template name or context also
    # template_name = "authapp/logout.html"
    # extra_context = {"status": "Log OUt success fully "}


# password change

class PasswordChange(PasswordChangeView):
    template_name = "authapp/pswdchng.html"
    # so here need to give url when our password will change then it will redirect on this page
    success_url = ("/customProfile/")

    def form_valid(self, form):
        messages.success(
            self.request, f'Your pasword changed successfully!')
        return super().form_valid(form)


# here we show password reset
class Pswreset(PasswordResetView):
    # it show a form where we give email for reset template
    template_name = "authapp/pswreset.html"
    # when we submit this email then it redirect to this url
    success_url = "Psw_reset_send_link"

# when we give email in password reset form then it will redirect on it for showing some info


class Pswreset_send_link(PasswordResetDoneView):
    template_name = "authapp/psw_reset_done.html"


class Psw_reset(PasswordResetConfirmView):
    template_name = "authapp/psw_reset_confirm.html"
    # when we reset confirm password then we redirect it on login page
    success_url = "/"


class Home(TemplateView):
    template_name = "authapp/home.html"


class CustomPF(TemplateView):
    template_name = "authapp/profile.html"
