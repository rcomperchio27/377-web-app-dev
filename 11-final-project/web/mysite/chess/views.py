from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Choice, Question, Game, User
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class GameIndexView(generic.ListView):
    template_name = "chess/index.html"
    context_object_name = "games_list"

    def get_queryset(self):
        """
        Return games in the Game table
        """
        return Game.objects.all()

class GameDetailView(generic.DetailView):
    model = Game
    template_name = "chess/detail.html"

    def get_queryset(self):
        return Game.objects.all()

class UserIndexView(generic.ListView):
    template_name = "chess/login.html"
    context_object_name = "user_list"

    def get_queryset(self):
        """
        Return users in the User table
        """
        return User.objects.all()

class UserDetailView(generic.DetailView):
    model = User
    template_name = "chess/detail.html"

    def get_queryset(self):
        return User.objects.all()

# class save(generic.ListView):
#     model = Game
#     template_name = "chess/save.html"
#     context_object_name = "games_list"

#     def get_queryset(self):
#         return Game.objects.all()
    
class GameResultsView(generic.ListView):

    model = Game
    context_object_name = "games_list"
    template_name = "chess/save.html"

    from django.views.decorators.http import require_http_methods

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        
        user = User.objects.get(pk=1)
        game = Game.objects.get(pk=pk)
        game_board = request.POST["board"]
        game_time_white = request.POST["white-time"]
        game_time_black = request.POST["black-time"]

        # game = Game(game_board=game_board, game_time_white=game_time_white, game_time_black=game_time_black, user_id=user)
        game.game_board = game_board
        game.game_time_white = game_time_white
        game.game_time_black = game_time_black
        
        game.save() 
        return HttpResponse(f"Post ID: {pk}, {game_board} ")
    
class UserLoginView(generic.ListView):

    model = User
    context_object_name = "user_list"
    template_name = "chess/login.html"

    from django.views.decorators.http import require_http_methods

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        
        user = User.objects.get(pk=pk)
        list_display = ["user_name", "user_games", "user_wins", "user_losses", "user_saved_game", "user_current_games"]
        user_name = request.POST["user-name"]
        game_time_white = request.POST["white-time"]
        game_time_black = request.POST["black-time"]

        # game = Game(game_board=game_board, game_time_white=game_time_white, game_time_black=game_time_black, user_id=user)
        game.game_board = game_board
        game.game_time_white = game_time_white
        game.game_time_black = game_time_black
        
        game.save() 
        return HttpResponse(f"Post ID: {pk}, {game_board} ")
    