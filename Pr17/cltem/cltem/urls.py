"""cltem URL Configuration

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
    # here we give template name so we don't need to write any views in our views .
    path("", views.TemplateView.as_view(template_name="clapp/home.html")),
    # here we new viewfunction name where we give templatename and context also
    path("custom", views.mytemplateview.as_view(), name="custom"),

    # here we give dynamic url in it
    path("custom/<int:cl>/", views.mytemplateview.as_view(), name="custom"),


]
