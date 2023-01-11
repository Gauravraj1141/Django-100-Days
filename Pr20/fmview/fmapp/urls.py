from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.MyFeedbackform.as_view(), name="fm"),
    path("thanku/", views.thanks.as_view(), name="thanks")
]
