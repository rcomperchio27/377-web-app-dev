import datetime

from django.db import models
from django.utils import timezone


from django.contrib import admin

class Game(models.Model):
    game_id = models.BigAutoField(primary_key=True)
    game_board = models.CharField(max_length=200)
    game_time_white = models.IntegerField(default=0)
    game_time_black = models.IntegerField(default=0)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=200)
    user_games = models.IntegerField(default=0)
    user_wins = models.IntegerField(default=0)
    user_losses = models.IntegerField(default=0)
    user_saved_game = models.IntegerField(default=0)
    user_current_games = models.IntegerField(default=0)

class Question(models.Model):
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):  
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
