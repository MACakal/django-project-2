from django import forms
from django.forms import DateInput
from .models import Profile, Game, Session


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'favoriteconsole', 'profile_picture']
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
        }

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ("name", "releaseyear", "console")

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['game', 'score', 'date']
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }