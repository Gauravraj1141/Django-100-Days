from django.shortcuts import render

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from storeapp.models import Products
from tagsapp.models import LabelTag


def home(request):
    # it will return this product contentype id
    queryset = ContentType.objects.get_for_model(Products)

# here we can use it for indentation
    LabelTag.objects.select_related("Lable").\
        filter(
        content_type=queryset,
        object_id=1
    )

    return render(request, "store/home.html")


def updatedata(request):
    # if we give it here without any filter or specific field then it will update all fiedls data  
    queryset = Products.objects.update(
        name="aalu", price=44.2, quantity=44)
    print(queryset)
    return render(request, "store/home2.html")
