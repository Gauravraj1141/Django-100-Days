from django.urls import path
from . import views

urlpatterns = [
    path("", views.home.as_view(), name="home"),
    path("update/<int:id>/", views.Update.as_view(), name="updates"),
    path("delete/<int:id>/", views.delete.as_view(), name="Delete"),
]
