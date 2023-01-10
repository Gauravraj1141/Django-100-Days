from django.shortcuts import render, redirect

# here we create crup project with the help of class based view
from django.views import View

# we can use template view and redirect view also

from django.views.generic import RedirectView, TemplateView

from .forms import studentform

from .models import User

# here we take tempalte view


class home(TemplateView):

    template_name = "clapp/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fm"] = studentform()
        context["mydata"] = User.objects.all()
        return context

    def post(self, request):
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


# in update we take inheri view
class Update(View):
    template = 'clapp/Update.html'

    def get(self, request, id):
        data = User.objects.get(UsId=id)
        form = studentform(instance=data)
        context = {"fm": form}
        return render(request, self.template, context)

    def post(self, request, id):
        data = User.objects.get(UsId=id)
        form = studentform(request.POST, instance=data)
        if form.is_valid():
            form.save()
        return redirect("/")

# in delete we take redirect view


class delete(RedirectView):
    url = "/"

    # we give id from url then it will come here in kwargs
    def get_redirect_url(self, *args, **kwargs):
        # print(kwargs) #{'id': 1}
        # here in kwargs id will be come in like it {'id': 1}
        myid = kwargs['id']
        User.objects.get(UsId=myid).delete()
        return super().get_redirect_url(*args, **kwargs)
