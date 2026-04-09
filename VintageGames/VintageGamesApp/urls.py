from django.urls import path, include
from . import views
from .models import Profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("", views.homepage, name="home"),
    path('', include('django.contrib.auth.urls')),
    path("games/", views.games, name="games"),
    path("register/", views.register, name="register")

]