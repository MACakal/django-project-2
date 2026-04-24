from django import forms
from django.forms import DateInput
from .models import Profile, Game, Session


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'favoriteconsole', 'date_of_birth', 'profile_picture']
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
        }

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ("name", "releaseyear", "console", "genre")

class SessionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Session
        fields = ['game', 'score', 'date']
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }

    def clean(self):
        cleaned_data = super().clean()
        game = cleaned_data.get('game')
        date = cleaned_data.get('date')
        if self.user and game and date:
            qs = Session.objects.filter(user=self.user, game=game, date=date)
            if self.instance and self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError(
                    "You already have a session for this game on this date."
                )
        return cleaned_data
