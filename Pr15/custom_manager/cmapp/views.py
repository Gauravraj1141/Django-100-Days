import random
from django.shortcuts import render, redirect

from .models import User, myuser, myuser_proxy
from faker import Faker
fake = Faker()


def generate(request):
    for i in range(20):
        name = fake.name()
        age = fake.random.randint(20, 60)
        marks = fake.random.randint(200, 900)
        # we made our custom manager so here we also use it
        data = User.custom.create(name=name, age=age, marks=marks)
        # but in my myuser model it have no custom name manager so we need to give here default manager name or our custom manager name

        data = myuser.mycustom.create(name=name, age=age, marks=marks)

    return redirect("/")


# def home(request):
#   # so here we change our manager name here we used objects before but now we change it now we use custom here
#     data = User.custom.all()
#     return render(request, "stuapp/index.html", {"data": data})


# def home(request):
#     # here we give our custom manager name so in it we apply filter so all the values it will fetch with apply filter which we give in it
#     data = myuser.mycustom.all()
#     return render(request, "stuapp/index.html", {"data": data})


# here we use this custom manage with our proxy model
def home(request):
    data = myuser_proxy.mycustom.all()
    return render(request, "stuapp/index.html", {"data": data})
