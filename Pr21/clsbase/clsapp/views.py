from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView


class home(TemplateView):
    template_name = "registration/home.html"
