from django.shortcuts import render

from django.contrib.auth.models import User

from .models import SinglePage, Book, Blog

from django.db.models import Q


def home(request):
    return render(request, "data/home.html")


def myuserdata(request):
    All_user = User.objects.all()
    # user who write book that's price is more than 400
    # we use here lookups for finding particular users
    authoruser = User.objects.filter(mybook__Book_price__gt=400)

    # all users name who write 	Bewafai and A alone Django book
    # here we take this mybook it is related name from  book table we give there
    uniqueauthor = User.objects.filter(
        Q(mybook__Book_name='Bewafai') | Q(mybook__Book_name='A alone  Django'))
    # here we use ~ it means show those user who don't write these two books it is called negative Q
    # uniqueauthor = User.objects.filter(
    #     ~Q(mybook__Book_name='Ji Bolti na') | ~Q(mybook__Book_name='hey we are coder'))

    context = {"alldata": All_user, "author": authoruser,
               "unique_author": uniqueauthor}
    return render(request, "data/showusers.html", context)


def Pagedata(request):

    Allpagedata = SinglePage.objects.all()

    # show pages those make in 2023 or after 2022
    somepages = SinglePage.objects.filter(Page_date__year=2023)
    # show pages those make in 2022 or before 2023
    # somepages = SinglePage.objects.filter(Page_date__year__lt=2023)
    # or we can write it as like
    pagesbefore = SinglePage.objects.filter(Page_date__year=2022)

    # pages that make  after jan and before september in 2022
    normpages = SinglePage.objects.filter(Q(Page_date__month__gt=1) & Q(
        Page_date__month__lt=9) & Q(Page_date__year=2022))

    # page that makes attif rdx and guarav
    # so here we take User's  table reference for fetching pages so we can do this type
    selectpage = SinglePage.objects.filter(
        Q(Page_author__email="rdx114@gmail.com") | Q(Page_author__username="Aatif") | Q(Page_author__username="gaurav"))

    context = {"Alldata": Allpagedata,
               "somepage": somepages, "before": pagesbefore, "norm": normpages, "users": selectpage}
    return render(request, "data/showpages.html", context)


def Bookdata(request):
    All_Book = Book.objects.all()

    # show books which prices are greater than 300 and less than 800
    lowpricebook = Book.objects.filter(
        Q(Book_price__gt=300) & Q(Book_price__lt=800))

    # show some books which are written by guarav attif and sachin
    bookbyname = Book.objects.filter(
        Book_authors__username='gaurav') & Book.objects.filter(Book_authors__username='Rdx') & Book.objects.filter(Book_authors__username='Aatif')

    print(bookbyname)

    context = {"alldata": All_Book,
               "pricebook": lowpricebook, "bookbyname": bookbyname}
    return render(request, "data/showbooks.html", context)


def Blogdata(request):

    allblogdata = Blog.objects.all()
    # show all blogs which are add in 2023
    latestblog = Blog.objects.filter(Blog_pub_date__year=2023)

    # some blogs which is added by rdx
    bypersonblog = Blog.objects.filter(
        Q(Blog_author__username="Rdx") & Q(Blog_pub_date__year=2022))

    context = {"alldata": allblogdata,
               'latest': latestblog, "rdx": bypersonblog}
    return render(request, "data/showblog.html", context)
