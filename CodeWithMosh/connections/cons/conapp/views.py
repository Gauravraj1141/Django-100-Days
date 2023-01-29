from django.shortcuts import render

# Create your views here.
from .models import Products

from django.db import connection

# we can use cursor also

# we can use cursor alongwith with method


def home(request):
    # here we don't need to close it with with method
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO conapp_products  VALUES(5,'marker',555)")

    return render(request, "cons/index.html")


'''
def home(request):

    # HERE    it is a cursor method we need to close it if we execute query
    cursor = connection.cursor()
    cursor.execute("INSERT INTO conapp_products  VALUES(44,'PENDISL',555)")
    cursor.close()

    return render(request, "cons/index.html")'''


'''def home(request):
    # we can give here complex query of sql also 
    # queryset = Products.objects.raw("select * from conapp_products")
    queryset = Products.objects.raw("select price from conapp_products ")

    return render(request, "cons/index.html", {'result': queryset})
'''
