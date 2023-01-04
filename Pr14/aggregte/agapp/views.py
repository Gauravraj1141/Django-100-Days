from django.db.models import Q
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
    # studata = students.objects.all()

    # here we are using q object in queryset
    # here we use & operator
    # studata = students.objects.filter(Q(id__gte=3) & Q(marks__gte=250))

    # now we use or operator |
    # studata = students.objects.filter(Q(id__gte=3) | Q(marks__gte=250))

    # ++++++++++++++++++++++++++++++++++++++++++++++
    # LIMIted query set
    # it is for first 5 values
    # so we can show some limited values by this slicing
    # studata = students.objects.all()[:5]

    studata = students.objects.all()[:20]
    marksavg = studata.aggregate(Avg("marks"))
    marksum = studata.aggregate(Sum("marks"))
    marksmin = studata.aggregate(Min("marks"))
    markcount = studata.aggregate(Count("marks"))
    markmax = studata.aggregate(Max("marks"))
    print(marksavg)

    return render(request, 'stuapp/table.html', {"data": studata, "avg": marksavg, "sum": marksum, 'min': marksmin, "count": markcount, "max": markmax})
