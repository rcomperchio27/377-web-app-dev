from django import forms
from .models import Game, User

class YourModelForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['game_time', 'game_board'] # Columns to update
