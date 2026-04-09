<<<<<<< HEAD

from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("", views.homepage, name="index"),

=======
from django.urls import path,include
from . import views

urlpatterns = [

    path("", views.indexTest, name="index"),
>>>>>>> makeModelsForGamesAndSession
]