from django import forms
from .models import User


class studentform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Name', 'Email', 'Phone', ]
        error_messages = {"Name": {"required": "Name is required"}}
        widgets = {
            'Name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Name.."}),
            'Email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Email.."}),
            'Phone': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Phone no.."}),
        }
