from django.shortcuts import render

# Create your views here.


def home(request):
    # it will give us 0 and then when we refresh page then this fun run and value of count will increase and show increased value
    ct = request.session.get("count", 0)
    pgcount = ct + 1
    request.session["count"] = pgcount
    return render(request, "pageapp/index.html", {"c": ct})
