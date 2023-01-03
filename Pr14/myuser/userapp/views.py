from django.shortcuts import render, HttpResponse
from .models import students
# Create your views here.
from faker import Faker
import random

fake = Faker()


def home(request):
    for i in range(100):
        name = fake.name()
        Address = fake.address()
        Email = fake.email()
        Phone = fake.phone_number()
        roll = fake.random.randint(10, 99)
        data = students.objects.create(
            Name=name, Email=Email, Phone=Phone, Address=Address, roll=roll)

    return render(request, "stuapp/index.html")


def table(request):
    userdata = students.objects.all()
    # userdata = users.objects.all().filter(Name="Seth Perkins")

    return render(request, "stuapp/table.html", {"data": userdata})
