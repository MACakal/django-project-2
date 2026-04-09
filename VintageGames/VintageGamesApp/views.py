from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import GameForm, SessionForm, ProfileForm, Session
from .models import Game
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import F

# Create your views here.
def homepage(request):
    return render(request, "base/index.html")

def games(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'base/games.html', context)

def register(requests):
    if requests.method == "POST":
        form = UserCreationForm(requests.POST)
        if form.is_valid():
            user = form.save()
            login(requests, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    context = {"form":form}
    return render(requests, "registration/register.html", context)