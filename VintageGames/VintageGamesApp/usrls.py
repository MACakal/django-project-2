from django.urls import path,include
from . import views

urlpatterns = [

    path("", views.indexTest, name="index"),
]