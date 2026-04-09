from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.homepage, name="home"),
    path('', include('django.contrib.auth.urls')),
    path("games/", views.games, name="games"),
    path("register/", views.register, name="register"),
    path("suggest_game/", views.suggest_game, name="suggest_game"),
    path("unapproved_games/", views.unapproved_games, name="unapproved_games"),
    path("new_sessions/", views.new_sessions, name="new_sessions"),
    path("my_sessions/", views.my_sessions, name="my_sessions"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("newsfeed/", views.newsfeed, name="newsfeed"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)