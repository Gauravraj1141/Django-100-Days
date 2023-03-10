from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


# registration form
class Registrationform(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {"email": "Email"}


# user login for here we give some bootstrap classes in our form

class user_login_form(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control form-control-lg"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control form-control-lg"}))


class user_profile_change(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']



# we create here it for admin means all field will be watch by admin and change anything and any user access means admin can make any user superuser so we give all access to the admin in our frontend view 

class Admin_profile_view(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = "__all__"
        labels = {"email": "Email"}
