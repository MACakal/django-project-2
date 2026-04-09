from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import GameForm, SessionForm, ProfileForm, Session
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import F

# Create your views here.
def homepage(request):
    return render(request,"index.html")
