from django.shortcuts import render

# class based views

from django.views import View

from .forms import register

# here we inherit the our views from View


class myview(View):

    # here we define get method for get request
    def get(self, request):
        # give any context in it
        context = {"name": "Gaurav Rajput"}
        return render(request, "clapp/home.html", context)


# how to handle get and post reqeust
# here we don't need to give if else condition in get and post instead we give only direct function get and post and more other also
class registration(View):
    # this function is for get request
    def get(self, request):
        # it is our form
        form = register()
        context = {"fm": form}
        return render(request, "clapp/register.html", context)

    # this function is for post request
    def post(self, request):
        formdata = register(request.POST)
        if formdata.is_valid():
            mydata = formdata.cleaned_data["name"]
        context = {"fmdata": mydata}
        return render(request, "clapp/showuser.html", context)


# we use this single view with multiple urls with the help of giving dynamic templates
class testingurl(View):
    # here we need define  variable for template
    template = ""
    # this function is for get request

    def get(self, request):
        # we give here empty name because we give it dynamcally
        context = {"myname": "rajputana"}
        return render(request, self.template, context)


####################################################################
# here we create functionbase view for giving tempalte name dynamically


def myfunc1(request, template):
    context = {"Name": "rajputana club"}
    return render(request, template, context)
