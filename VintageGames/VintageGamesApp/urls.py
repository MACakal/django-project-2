from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path("", views.homepage, name="home"),
    path('', include('django.contrib.auth.urls')),
    path("games/", views.games, name="games"),
    path("register/", views.register, name="register"),
    path("suggest_game/", views.suggest_game, name="suggest_game"),
    path("unapproved_games/", views.unapproved_games, name="unapproved_games"),
    path("approve_game/<int:pk>/", views.approve_game, name="approve_game"),
    path("new_sessions/", views.new_sessions, name="new_sessions"),
    path("my_sessions/", views.my_sessions, name="my_sessions"),
    # admin all sessions 
    path("my_sessions_admin/", views.my_sessions_admin, name="my_sessions_admin"),
    path("edit_session/<int:pk>/", views.edit_session, name="edit_session"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path(
        "password-change/",
        PasswordChangeView.as_view(
            template_name="base/change_password.html",
        ),
        name="password_change",
    ),
    path("newsfeed/", views.newsfeed, name="newsfeed"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)