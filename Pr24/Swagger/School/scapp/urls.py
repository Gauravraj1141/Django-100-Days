
from django.urls import path
from scapp.Api.myschool.views_schlstaff import SchlStaff


urlpatterns = [

    path("staff", SchlStaff.as_view(), name="staff")
]
