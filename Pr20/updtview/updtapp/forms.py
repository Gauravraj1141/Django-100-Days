from .models import Locker


from django import forms


class mycustomform(forms.ModelForm):
    class Meta:
        model = Locker
        fields = ('Username', 'Email', 'Password', )
        widgets = {"Username": forms.TextInput(
            attrs={"class": "form_control"}), "Password": forms.PasswordInput(render_value=True, attrs={"class": "form_password"})}
