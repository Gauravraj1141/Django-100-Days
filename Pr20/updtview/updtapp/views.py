from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .forms import mycustomform
from .models import Locker
from django.urls import reverse


class Createmynewview(CreateView):
    # here we use customform
    form_class = mycustomform
    template_name = "updapp/home.html"

    # we give in models so we don't give here
    # success_url = "/thankscreate/"

# here we create our update view


class Updatemyview(UpdateView):
    # here we must give model name with our custom form name it will take that pk or id or slug in backgroud
    model = Locker
    form_class = mycustomform
    template_name = "updapp/home.html"

# here we redirect it also where we redirect create view by models.py
    def get_absolute_url(self):
        return reverse("thankscreate", kwargs={"pk": self.pk})


class Thankscreateview(DetailView):
    model = Locker
    template_name = "updapp/thankscreate.html"
    context_object_name = "user"
