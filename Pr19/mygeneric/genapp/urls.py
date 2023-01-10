
from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.mylistview.as_view(), name="myhome")
]
