from django import forms
from .models import ZoneSchools


class mycustomform(forms.ModelForm):
    class Meta:
        model = ZoneSchools
        fields = ['name', 'address', 'Contact_no', ]
