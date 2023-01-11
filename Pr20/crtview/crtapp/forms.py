from django import forms
from .models import ZoneSchools


class mycustomform(forms.ModelForm):
    class Meta:
        model = ZoneSchools
        fields = ['name', 'address', 'Contact_no', ]
        widgets = {"name": forms.TextInput(
            attrs={"class": "mynewform"}), "address": forms.TextInput(attrs={"class": "mynewform", "placeholder": 'enter your address'})}
