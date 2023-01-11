from django.shortcuts import render
# we import detailview for show the particular user's data
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import mystudents

# it is detailview for showing only one user's data


class studentdata(DetailView):
    model = mystudents
    template_name = "stuapp/showdata.html"

    # here we give custom context name here data will here
    context_object_name = "studata"
    # here we give custom url id we must give pk and slug but here we give custom name
    pk_url_kwarg = "mystuid"

    # here we can give more context data for showing list of users

    def get_context_data(self, **kwargs):
        # we can get user pk or slug here this type
        object = self.get_object()
        pk = object.pk

        context = super().get_context_data(**kwargs)
        context['RestUsers'] = mystudents.objects.exclude(stu_id=pk)
        return context


# it is list view for showing all user's data

class allstudetns(ListView):
    model = mystudents
    template_name = 'stuapp/home.html'
    context_object_name = "allusers"
