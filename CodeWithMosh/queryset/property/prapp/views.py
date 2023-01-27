from django.forms import IntegerField
from django.shortcuts import render

from django.db.models import Q, Value, F, Func, Count, ExpressionWrapper
from .models import PropertyOwner, OwnerDetails
import faker
import random
from django.db.models.functions import Concat
Fake = faker.Faker()


def DetailsFill(request):
    for i in range(100):
        name = Fake.name()
        phone = Fake.phone_number()
        email = Fake.email()
        address = Fake.address()
        price = random.randint(1, 50000)
        property_owner = PropertyOwner.objects.create(name=name, price=price)
        for i in range(10):
            ow = OwnerDetails(
                name=name, email=email, phone=phone, address=address)
            ow.save()
            ow.property.add(property_owner)

    return render(request, "prapp/home.html", {"data": "successfully created"})


def ShowData(request):
    # Detail = OwnerDetails.objects.all()
    # Detail = OwnerDetails.objects.filter(
    #     Q(property__price__gte=500000) & Q(name__istartswith="G"))
    # Detail = OwnerDetails.objects.values(
    #     'name', 'id', 'phone', 'property__name')
    # Detail = OwnerDetails.objects.values_list(
    #     'name', 'id', 'phone', 'property__name', 'property__price').order_by('name').filter(Q(property__price__gte=2000) & Q(property__price__lte=10000))
    # Detail = OwnerDetails.objects.only('property__name')
    # Detail = OwnerDetails.objects.filter(
    #     property__id=11).distinct()

    # very good query for saving more queries
    # if we use foreignkey field then we should use this select_related methods
    # Detail = OwnerDetails.objects.select_related('PropertyOwner').all()

    # if we use many to manay relation then we should use this prefetch_related field
    # Detail = OwnerDetails.objects.prefetch_related('property').all()

    # this query will give us only property details
    # Detail = PropertyOwner.objects.prefetch_related('ownerdetails_set').all()

    # Annotate method we can add new column in our table with the help of it and expression like : value , F method , func and aggregate also
    # so here we can give field name and give expression
    # Detail = OwnerDetails.objects.annotate(new_field=Value(2)+1)

    # here we can concat first and last name of our user with this annotate and func used
    # Detail = OwnerDetails.objects.annotate(nameandemail=Func(
    #     F("name"), Value("  "), F("name"), function='CONCAT'))
    # Detail = OwnerDetails.objects.annotate(
    #     Fullname=Concat("name", Value(" "), "name"))

    # we can see how many property own by any owner
    # Detail = OwnerDetails.objects.filter(
    #     name="Cheryl Carter").annotate(property_count=Count('property'))

    # Here we will see expressiowrapper class and give some value in it it will give result in diff field which we want
    exwrapper = ExpressionWrapper(F("price")*3, output_field=IntegerField())

    Detail = PropertyOwner.objects.annotate(discount_price=exwrapper)
    print(Detail)
    return render(request, "prapp/home.html", {"data": Detail})
