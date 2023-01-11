from django.shortcuts import render, HttpResponse
from django.views.generic.edit import FormView

from django.views.generic import TemplateView

# we import our form here and give it inthis class
from .forms import feedbackform


class MyFeedbackform(FormView):
    template_name = "fmapp/home.html"

    # we give our form name
    form_class = feedbackform

    # when we submit our form then it will redirect on this url so we can give here
    success_url = "/thanku/"

    # we can get all values of our form

    def form_valid(self, form):
        # it returns a dictonary
        formdata = form.cleaned_data

        # {'Name': 'Gaurav Rajput', 'review': 'very good site', 'stars': 5}
        print(formdata)
        # we can save it in to data base
        # return super().form_valid(form)
        # and we can return response here also then success_url will not work
        return HttpResponse("hey it is form valid response your feedback is added successfully ")


class thanks(TemplateView):
    template_name = "fmapp/thankyou.html"
