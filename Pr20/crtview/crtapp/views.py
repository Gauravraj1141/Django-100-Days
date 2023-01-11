from .forms import mycustomform
from django.shortcuts import render
from django.views.generic import TemplateView

# here we import it for showing that particular entry which we enter now
from django.views.generic.detail import DetailView

# Generic edit class baseed createview
# here we see how to createview work : it will create a form and display in on tempalte and save data into database because it inherit formview also
from django.views.generic.edit import CreateView

# here we import model for generate our form with the help of createview

from .models import ZoneSchools


from django import forms
# it will automatically save the data into database


class RegisterSchools(CreateView):
    model = ZoneSchools
    # give fields for our form
    fields = ('name', 'address', 'Contact_no', )

    # we can add attributes in our form like class placeholder etc

    def get_form(self):
        form = super().get_form()
        form.fields["name"].widget = forms.TextInput(
            attrs={"class": "form-control"})
        form.fields["address"].widget = forms.TextInput(
            attrs={"class": "form-control"})
        form.fields["Contact_no"].widget = forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Your Phone"})

        return form

    template_name = "crtapp/home.html"

    # when our form data will save then we need to give url where redirect after submit form  instead it we give it in models.py also

    # success_url = "/added/"


class Successdata(TemplateView):
    template_name = "crtapp/success.html"


# so we can show detail view of that particular value which we add  in school table
class Showdetails(DetailView):
    model = ZoneSchools
    template_name = 'crtapp/showdata.html'
    context_object_name = "schlname"


# we add some fields in our form like upper class  instead it we can add these attributes in our form like it
# here we override our formview in createview


class mynewformview(CreateView):
    # here we give model form name which we create in our forms.py
    form_class = mycustomform
    template_name = "crtapp/cstmform.html"
