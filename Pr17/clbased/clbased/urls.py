"""clbased URL Configuration

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

from clapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.myview.as_view()),
    path("register", views.registration.as_view(), name="register"),
    # we can give template name here also and point this views also in another url
    path("sample", views.testingurl.as_view(
        template="clapp/mysample.html"), name="sample"),
    # here we give diff template name
    path("sample2", views.testingurl.as_view(
        template="clapp/mysample2.html"), name="sample2"),

    #######################################################
    # here we can give dynamic tempalte name in our views in function based views also
    path("myfunview", views.myfunc1, {
         "template": "clapp/funcview.html"}, name="myfunview"),

]
