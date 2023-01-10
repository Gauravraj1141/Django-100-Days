from django.shortcuts import render

from django.views.generic import TemplateView, RedirectView


# here we can create a view that redirect to the another page

class redirect_to_the_garadge(RedirectView):
    # url = "/garadge"
    # instead of url we can give pattern name as well
    pattern_name = "mygaradge"


# here we create a tempalte view that is for garadge

class grgaradge(TemplateView):
    template_name = 'clapp/mygaradge.html'


class students(TemplateView):
    template_name = 'clapp/clsstudents.html'


class newredirect(RedirectView):
    # here we give studetns pattern name
    pattern_name = "cls"
