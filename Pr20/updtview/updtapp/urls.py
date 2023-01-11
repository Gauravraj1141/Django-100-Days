from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Createmynewview.as_view(), name="home"),
    path('thankscreate/<int:pk>/',
         views.Thankscreateview.as_view(), name="thankscreate"),
    path('Updateview/<int:pk>/', views.Updatemyview.as_view(), name="Updateview"),
    path('Deleteview/<int:pk>/', views.DeleteMyview.as_view(), name="Deleteview"),
]
