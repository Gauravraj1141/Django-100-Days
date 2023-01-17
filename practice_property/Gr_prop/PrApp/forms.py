from django import forms

from .models import PropertyDetail, State, City


class PrForm(forms.ModelForm):

    State_name = forms.ModelChoiceField(queryset=State.objects.all(), empty_label="Select a State", to_field_name='st_id',
                                        widget=forms.Select(attrs={'class': 'form-control', 'onchange': 'getCities()'}))
    City_name = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="Select a city", to_field_name='ct_id',
                                       widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = PropertyDetail
        fields = ('Property_name', 'Property_address',
                  'State_name', 'City_name',)
        widgets = {"Property_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Write Property Name.."}),
                   "Property_address": forms.TextInput(attrs={"class": "form-control", "placeholder": "Write Address .."})}
