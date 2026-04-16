from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm,SessionForm

def homepage(request):
    return render(request, "base/index.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "registration/register.html", context)

@login_required
def games(request):
    return render(request, "base/games.html")

@login_required
def suggest_game(request):
    return render(request, "base/suggest_game.html")

@staff_member_required
def unapproved_games(request):
    return render(request, "base/unapproved_games.html")

@login_required
def new_sessions(request):
    profile = request.user.profile
    if request.method == "POST":
        form = SessionForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("new_sessions")
    else:
        form = SessionForm(instance=profile)

    context = {
        "form": form,
        "profile": profile
    }
    return render(request, "base/add_sessions.html",context)

@login_required
def my_sessions(request):
    return render(request, "base/my_sessions.html")

@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProfileForm(instance=profile)

    context = {
        "form": form,
        "profile": profile
    }
    return render(request, "base/edit_profile.html", context)

@login_required
def newsfeed(request):
    return render(request, "base/newsfeed.html")