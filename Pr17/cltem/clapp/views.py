from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


# here is a templateview we can not need to render it anywhere it helps us when we render only simple template without giving anylogic in view.
# we can easily inherit templateview for render template in class based view

class mytemplateview(TemplateView):
    template_name = "clapp/custom.html"

    #  here we give context in our template

    def get_context_data(self, **kwargs):
        # we inherit parent context data
        context = super().get_context_data(**kwargs)
        print(context)
        context["name"] = "Gaurav rAjput"
        context["Class"] = "Bsc"
        context["roll"] = 22
        print(context)
        return context
