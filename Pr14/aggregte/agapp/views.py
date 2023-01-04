from django.db.models import Avg, Sum, Min, Max, Count
from django.shortcuts import render
from .models import students
# Create your views here.
from faker import Faker
import random
fake = Faker()


def dataset(request):
    for i in range(5):
        name = fake.name()
        marks = fake.random.randint(200, 300)
        setdata = students.objects.create(name=name, clname=name, marks=marks)
    return render(request, "stuapp/index.html")


def home(request):
    studata = students.objects.all()
    marksavg = studata.aggregate(Avg("marks"))
    marksum = studata.aggregate(Sum("marks"))
    marksmin = studata.aggregate(Min("marks"))
    markcount = studata.aggregate(Count("marks"))
    markmax = studata.aggregate(Max("marks"))
    print(marksavg)

    return render(request, 'stuapp/table.html', {"data": studata, "avg": marksavg, "sum": marksum, 'min': marksmin, "count": markcount, "max": markmax})
