from django.shortcuts import render
from .models import Blogs

# here we use paginator it will show our content  in different pages
from django.core.paginator import Paginator


def home(request):
    myblg = Blogs.objects.all()
    # here we give our object in this paginator and it will show by page
    mypages = Paginator(myblg, 4)
    paginator = mypages.page(1)
    print(paginator.count)
    print(paginator.number)  # 1
    print(paginator.has_previous())  # False
    print(paginator.has_next())  # True
    print(paginator.next_page_number())  # 2
    context = {'pages': paginator}
    return render(request, "pgapp/home.html", context)
