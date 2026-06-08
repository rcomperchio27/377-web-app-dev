from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Choice, Question, Game, User
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

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
        if request.POST["new-game"] == "false":
            pk = kwargs.get('pk')
            
            game = Game.objects.get(pk=pk)
            user = User.objects.get(user_name=request.POST["user"])
            game_board = request.POST["board"]
            game_time_white = request.POST["white-time"]
            game_time_black = request.POST["black-time"]
            game_id = pk - 1
            game.game_board = game_board
            game.game_time_white = game_time_white
            game.game_time_black = game_time_black
            id = game.game_id
            
            game.save() 
            return redirect(f"/chess/{id}/")
            # return HttpResponse(f"Post ID: {pk}, {game_board} ")
        else:
            user = User.objects.get(user_name=request.POST["user"])
            game_board = request.POST["board"]
            game_time_white = request.POST["white-time"]
            game_time_black = request.POST["black-time"]
            game = Game(game_board=game_board, game_time_white=game_time_white, game_time_black=game_time_black, user_id=user)
            game.save()
            id = game.game_id
            return redirect(f"/chess/{id}/")
    
class UserLoginView(generic.ListView):

    model = User
    context_object_name = "user_list"
    template_name = "chess/login.html"

    from django.views.decorators.http import require_http_methods

    def post(self, request, *args, **kwargs):
        # list_display = ["user_name", "user_games", "user_wins", "user_losses", "user_saved_game", "user_current_games"]
        # user = User.objects.get(pk=pk)
        user_name = request.POST["name"]
        login = False
        try:
            User.objects.get(user_name=user_name)
            user_exist = True
        except:
            user_exist = False
        if user_exist == True:
            user = User.objects.get(user_name=user_name)
            if check_password(str(request.POST["password"]), user.user_password):
                pk = user.pk
                
                id = user.user_id
                return redirect(f"/chess/{id}/login")
        else:
            user_password = str(request.POST["password"])
                
            hashed = make_password(user_password)
            user = User(user_name=user_name, user_password=hashed)
            game = Game(game_board="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", game_time_white=600, game_time_black=600, user_id=user)
            user.save() 
            game.save()
            id = game.game_id
            return redirect(f"/chess/{id}/")
    