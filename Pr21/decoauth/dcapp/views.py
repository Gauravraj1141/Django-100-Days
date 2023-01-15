from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required

# here we need to give decorator use method_decorator
from django.utils.decorators import method_decorator


class Profile(TemplateView):
    template_name = "registration/home.html"


class Aboutpage(TemplateView):
    template_name = "registration/about.html"


# here we need to give this decorator and name dispatch also
@method_decorator(login_required, name='dispatch')
class Myproperty(TemplateView):
    template_name = "registration/property.html"
