from django.shortcuts import render, HttpResponse
from .models import students, teacher
# Create your views here.
from faker import Faker
import random

from datetime import date, time

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
        dt = fake.date_time()
        data = students.objects.create(
            Name=name, Email=Email, Phone=Phone, Address=Address, roll=roll, Dob=dob, dt=dt)
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
    # userdata = students.objects.filter(
    #     Q(roll__gt=30) | Q(Name__startswith="g"))

    # here one object return
    # it will return single object  if this value present in database otherwise it will return a error DoesNotExist at /Table
    # so get will occur error when value is not present in database or more than one value present in database  here only one value unique value will get by get method
    # userdata = teacher.objects.get(id=2)

    # first method : it will return first value of the database and we can user any filter or order
    # so it returns last value by id we give decesnding order
    # userdata = teacher.objects.order_by("-id").first()
    # last() it will return last value of this table so it returns first value of this table because we use decesnding order by id
    # userdata = teacher.objects.order_by("-id").last()

    # latest
    # so it returns latest date from the table data it returns very latest data 26 april 2022
    # userdata = teacher.objects.latest("Dob")
    # earliest means very old data
    # userdata = teacher.objects.earliest("Dob")

    # exist ()   it return true or false if data is avaialable then it returns true otherwise false.
    # we can use it also it will also return value with name
    # userdata = teacher.objects.values_list("Name", named=True)
    # print(userdata.exists()) so it returns true becasue userdata have some value

    # userdata = students.objects.get(id=1)

    # +++++++++++++++++++++++++++++++++++++++++++++$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ###############################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # here we saw some important methods

    # # here we need to give two arguments userdata and created so created means if created then created true otherwise userdata will  get value always ./and it returns also a object not a query set
    # userdata, created = students.objects.get_or_create(
    #     Name="ramsign", Email="rajput@gmail.com", Phone='63541251522', Address="cislkdfkal yan purs", roll=22)

    # userdata = students.objects.filter(id=1505).update(
    # Name="Gaurav Singh", Address="Chandigarh") so it returns no of row which row it updates so it updates 1 field so it reutrn 1 also

    # so here we cahnges all names where roll no is greater than 22
    # udatedata = students.objects.filter(roll__gt=22).update(Name="Gaurav")
    # userdata = students.objects.all()

    # userdata1, updatedata = students.objects.filter(
    #     roll__gt=22).update_or_create(Name="Rajput Gaurav", defaults={"Name": "hey rajput ji"})
    # userdata = students.objects.all()

    # print(userdata.count()) count() return all numbers of object in the database
    # we can show sql query  in our terminal by this query property
    # print(userdata.query)

    #   ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #   ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    # Some Lookup Fields in query set \\
    # userdata = students.objects.filter(roll__gte=33)

    # exact means that particular value which is in this table so all the roll number where 45 all will show
    # userdata = students.objects.filter(roll__exact=45) # it  is case sensitive we add i in it then it will case insensitive
    # it  is case sensitive we add i in it then it will case insensitive
    # userdata = students.objects.filter(Name__exact="christina Hodge") it is case sensitive
    # userdata = students.objects.filter(
    #     Name__iexact="christina Hodge")  # it is case insensitive

    # it will show only where g is in this name it is case sensitive but here it will show case insensitive behaviour
    # userdata = students.objects.filter(Name__contains="G") #it is case sensitive
    # userdata = students.objects.filter(
    #     Name__icontains="G")  # it is case insensitive

    # it is in method so all id  which number is
    # userdata = students.objects.filter(id__in=[2, 5, 8, 9, 6, 3, 54])
    # userdata = students.objects.filter(roll__in=[44, 39, 65])

    # greater than ,  less than , less than equal to lte ,  greater than equal to gte
    # userdata = students.objects.filter(roll__gt=66)
    # userdata = students.objects.filter(roll__gte=88)
    # userdata = students.objects.filter(roll__lte=88)
    # userdata = students.objects.filter(roll__lt=88)

    # startswith and enswith it is case sensitive and we use i with it then it will case insensitive but in sqllite database it case insensitive
    # userdata = students.objects.filter(roll__startswith=8)
    # userdata = students.objects.filter(Name__startswith="ra")
    # userdata = students.objects.filter(Name__istartswith="ra")
    # userdata = students.objects.filter(Name__endswith="ra")
    # userdata = students.objects.filter(Name__iendswith="ra")
    # userdata = students.objects.filter(Name__endswith="er")

    # Date method range is show some date between we give here we can use this type
    # userdata = students.objects.filter(Dob__range=(
    #     "2015-01-01", "2023-01-01")).order_by("Dob")

    # it is only for datatime field and we need to import data and time for checking it
    # userdata = students.objects.filter(dt__date=date(2015, 1, 2))
    # userdata = students.objects.filter(dt__date__gt=date(2015, 1, 2))

    # we can check year also in date field and datetime field also so we can check year month and day also in date field and datetimfield also
    # userdata = students.objects.filter(Dob__year=2015)
    # userdata = students.objects.filter(Dob__year__gt=2015)
    # userdata = students.objects.filter(Dob__year__gte=2015)

    # userdata = students.objects.filter(Dob__month=5)
    # userdata = students.objects.filter(Dob__month__gte=5)
    # userdata = students.objects.filter(Dob__day=5)
    # userdata = students.objects.filter(dt__day=5)
    # userdata = students.objects.filter(dt__week=6)
    # userdata = students.objects.filter(dt__week_day__gt=6)
    # so it gives all months from quearter 3
    # userdata = students.objects.filter(dt__quarter=3)
    # userdata = students.objects.filter(dt__quarter__gt=3)

    # userdata = students.objects.filter(dt__time__gt=time(12, 50))

    # userdata = students.objects.filter(dt__hour=0)
    # userdata = students.objects.filter(dt__hour__gt=0)
    # userdata = students.objects.filter(dt__minute=5)
    userdata = students.objects.filter(dt__second=5)

    print(userdata)
    print(userdata.query)

    return render(request, "stuapp/table.html", {"data": userdata})
    # it is only for one object because in table.html we use for loop but here we don't need for loop
    # return render(request, "stuapp/showobj.html", {"mydata": userdata})
