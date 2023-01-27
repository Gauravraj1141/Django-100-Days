from django.urls import path, include
from . import views

urlpatterns = [
    path("profile/", views.home.as_view()),
]
