from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm,SessionForm,GameForm
from .models import Game,Session

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
    games = Game.objects.filter(approved=True)
    context = {"games": games}
    return render(request, "base/games.html",context)

@login_required
def suggest_game(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            if request.user.is_staff:
                game.approved = True
                game.approvedby = request.user
                messages.success(request, " Admin added Game")
            else:
                game.approved = False
                messages.success(request, "Game suggestion submitted for review.")
            game.save()
            form = GameForm()
            return render(request, "base/suggest_game.html", {"form": form})
    else:
        form = GameForm()
    return render(request, "base/suggest_game.html", {"form": form})

@staff_member_required
def unapproved_games(request):
    games = Game.objects.filter(approved=False)
    context = {"games": games}
    return render(request, "base/unapproved_games.html",context)

@staff_member_required
def approve_game(request, pk):
    game = Game.objects.get(pk=pk, approved=False)
    game.approved = True
    game.approvedby = request.user
    game.save()
    messages.success(request, f"'{game}' approved!")
    return redirect("unapproved_games")


@login_required
def new_sessions(request):
    if request.method == "POST":
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user         
            session.save()                    

            messages.success(request, "Session added successfully")
            return redirect("my_sessions")
    else:
        form = SessionForm()

    context = {"form": form}
    return render(request, "base/add_sessions.html", context)

@login_required
def my_sessions(request):
    sessions = Session.objects.filter(user=request.user).order_by('-date')
    context = {"sessions": sessions}
    return render(request, "base/my_sessions.html", context)

# admin
@staff_member_required
def my_sessions_admin(request):
    if request.method == "POST":
        if request.POST.get("delete") and request.POST.get("session_id"):
            session_id = request.POST["session_id"]
            session = get_object_or_404(Session, pk=session_id)
            session.delete()
            messages.success(request, "Session deleted successfully")
            return redirect("my_sessions_admin")
    
    sessions = Session.objects.all()
    context = {"sessions": sessions}
    return render(request, "base/show-all-sessions-admin.html", context)

@login_required
def edit_session(request, pk):
    session = get_object_or_404(Session, pk=pk)
    if request.method == "POST":
        if request.POST.get("delete"):
            session.delete()
            messages.success(request, "Session deleted")
            return redirect("my_sessions")

        form = SessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            messages.success(request, "Session updated successfully")
            return redirect("my_sessions")
    else:
        form = SessionForm(instance=session)
    context = {"form": form, "edit": True}
    return render(request, "base/edit_session.html", context)

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
    sessions = Session.objects.exclude(user=request.user).select_related('game', 'user', 'user__profile').order_by('-date')
    return render(request, "base/newsfeed.html", {"sessions": sessions})

