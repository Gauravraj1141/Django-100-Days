from django.shortcuts import render, HttpResponse
from .models import students, teacher
# Create your views here.
from faker import Faker
import random

from django.db.models import Q

fake = Faker()


def home(request):
    for i in range(100):
        name = fake.name()
        Address = fake.address()
        Email = fake.email()
        Phone = fake.phone_number()
        roll = fake.random.randint(10, 99)
        dob = fake.date_of_birth()
        salary = fake.random.randint(3000, 9999)
        data = students.objects.create(
            Name=name, Email=Email, Phone=Phone, Address=Address, roll=roll, Dob=dob)
        data2 = teacher.objects.create(
            Name=name, Email=Email, Phone=Phone, Salary=salary, Dob=dob)

    return render(request, "stuapp/index.html")


def table(request):
    # userdata = students.objects.all()
    # userdata = students.objects.all().filter(Name="Seth Perkins")
    # roll number is greaterthen 30
    # userdata = students.objects.all().filter(roll__gt=30).order_by('Name')
    # roll number is lessthen 30
    # userdata = students.objects.all().filter(roll__lt=30).order_by('Name')

    # here data will show by name means all capital letter a to z series name will show because it is based on utf-16
    # userdata = students.objects.all().order_by('Name')

    # if we want some people whose age is greater than 20 and less than 30
    # userdata = students.objects.all().filter(
    #     Dob__lt="2003-01-01", Dob__gt="1993-01-01", Name__startswith="k")
    # we can delete all data from database
    # userdata = students.objects.all().delete()

    # exclude means where name startswith gar which all will not show and other will show
    # so we give roll greater than 44 so all roll number in this list will lessthan 44.
    # userdata = students.objects.exclude(roll__gt=44)

    # here we give order by roll number so all the list data willshow assending order and it is by default in this order by function
    # userdata = students.objects.order_by("roll")

    # and is we want to show all the roll numbers in desending order so we need to add - in this roll ,  here we add this minuse in roll so all the roll numbers will show in descending order

    # userdata = students.objects.order_by("-roll")

    # here we give ? so it list will show randomly numbers without order when we refresh the page then randomly show list not arrange
    # userdata = students.objects.order_by("?")

    # we apply order by in name so in the name a name starts with a will show in the last because it's first letter is small a and small a unicode value is greater than all the capital letter's value so we here all capital a will show in the first
    # userdata = students.objects.order_by("Name")

    # here reverse function will show all values reverse if we use order by so we can slicing the rows with it so here it show last 6 rows data
    # userdata = students.objects.order_by("roll").reverse()[:6]
    # userdata = students.objects.order_by("roll")[:8]

    # by the values function all the values will show in terminal because it return dictonary not a object
    # userdata = students.objects.values()

    # if we want show some specific fields like name and roll no only so we use ths value funciton and give all specific field which we want
    # userdata = students.objects.values("Name", "roll")

    # studentdata = students.objects.values('id',
    #                                       "Name", "Phone")
    # teacherdata = teacher.objects.values('id',
    #                                      "Name", "Phone")
    # it will combine these both table data and show all fields because we give all-true if we don't give true then it will show only name at one time in both table
    # userdata = teacherdata.union(studentdata)

    # intersection  it means where these both fields are same then it will show
    # intersection means like two name with same phone number will present in both tables so these will shwo so ye dono tables ka common data dega

    # userdata = teacherdata.intersection(studentdata)

    # difference
    # userdata = studentdata.difference(teacherdata)

    # we use here operators & | and Q
    # we use here & (and) operator

    # userdata = students.objects.filter(
    #     roll=23) & students.objects.filter(Name__startswith="y")
    # we can give here as like so we don't need and operator
    # userdata = students.objects.filter(
    #     roll=23, Name__startswith="y")

    # it is a or | operator
    # userdata = students.objects.filter(
    #     roll=23) | students.objects.filter(Name__startswith="y")

    # and we use these both operator in q

    # we need to import q

    # userdata = students.objects.filter(
    # Q(roll__gt=30) & Q(Name__startswith="g"))
    userdata = students.objects.filter(
        Q(roll__gt=30) | Q(Name__startswith="g"))

    print(userdata)
    # we can show sql query  in our terminal by this query property
    print(userdata.query)

    return render(request, "stuapp/table.html", {"data": userdata})
