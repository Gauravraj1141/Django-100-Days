from django.shortcuts import render
from django.views.generic.list import ListView
from .models import student

# it is generic view we see listview here we don't need to write more for show our data from model in our tempalte


class mylistview(ListView):
    model = student

    # here default tempalte name is = "appname/modelname_list.html"
    # and we can change this suffix name by
    # template_name_suffix = "_data"  # bydefault : "_list"
    # so now our tempalte name is according to our app and model : 'genapp/student_data.html'

    # now we give here custom name
    template_name = "genapp/home.html"

    # and context  is by default = student_list    but we can change it also

    context_object_name = "studentdata"

    # we can set ordering here also

    ordering = ["section"]

    # if we give more filter and more lookups in our queryset then we write this function
    def get_queryset(self):
        # here we override default queryset
        # return student.objects.filter(section__in=["a", "b"])
        # return student.objects.filter(name__startswith="om")
        return student.objects.filter(marks__gte=400)

    # and if we want to give some extra context then we need to override this function

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contextdata"] = student.objects.all()
        return context

    def get_template_names(self):
        # here we change tempalte name and we set this cookies in browser and here we can give new conditions
        if self.request.COOKIES["user"] == "gaurav":
            template_name = "genapp/gaurav.html"
            print("ye gaurav h")
        else:
            template_name = self.template_name
            print("ye home h")
        return template_name
