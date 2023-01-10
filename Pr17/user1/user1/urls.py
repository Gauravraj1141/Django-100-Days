"""user1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.TemplateView.as_view(
        template_name="clapp/home.html"), name="myhome"),

    # here we give redirectview so when we give index in the url then it redirect us on to the home page
    path("index", views.RedirectView.as_view(url="/"), name="index"),
    # here we give our custom redirect view which is redirect to the another view
    # if we give carhome then it will redirect to the garadge
    path("carhome", views.redirect_to_the_garadge.as_view(), name="carhome"),

    # here we create a template view

    path("garadge", views.grgaradge.as_view(), name="mygaradge"),


    # it is for int
    # path("mystu/<int:roll>/", views.students.as_view(), name="cls"),

    # here we give slug
    path("mystu/<slug:roll>/", views.students.as_view(), name="cls"),

    # path("students/<int:roll>/", views.newredirect.as_view(), name="mystu")
    # and we can give only int value in this url
    # so it we give any number in this url then it will redirect on this cls pattern name and show point out that template
    # path("<int:roll>/", views.newredirect.as_view(), name="mystu")
    # and we can give slug in this means str value

    path("<slug:roll>/", views.newredirect.as_view(), name="mystu")



]
