from django.urls import path
from . import views
urlpatterns = [
    path('', views.RegisterSchools.as_view(), name="home"),
    # path('added/', views.Successdata.as_view(), name="added"),
    # here we give because we give url in model
    path('Mydata/<int:pk>/', views.Showdetails.as_view(), name="Mydata"),

    path("newcustomform", views.mynewformview.as_view(), name="newform"),
]
