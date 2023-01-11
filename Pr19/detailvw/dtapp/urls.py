from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.allstudetns.as_view(), name="allstu"),

    # here we need to give an id or slug also because detailview can fetch only one user data means particular data
    # here we must give pk or slug by default but if we want to give custom name then we give custom value in view
    path("student/<int:mystuid>/", views.studentdata.as_view(), name="student"),



]
