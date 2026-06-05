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
    template_name = "chess/index.html"
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

class save(generic.ListView):
    model = Game
    template_name = "chess/save.html"
    context_object_name = "games_list"

    def get_queryset(self):
        return Game.objects.all()
    

# from .forms import YourModelForm

# def update_data(request, pk):
#     # Fetch the specific row you want to update using its primary key
#     instance = get_object_or_404(Game, pk=0)
#     print(instance)
#     if request.method == 'POST':
#         # Bind the submitted data and existing instance to the form
#         form = YourModelForm(request.POST, instance=instance)
#         if form.is_valid():
#             form.save() # This updates the existing row in your database
#             return redirect('success_url') # Redirect to a success page
#     else:
#         form = YourModelForm(instance=instance)
        
#     return render(request, 'chess/save.html', {'form': form})

class GameResultsView(generic.ListView):

    model = Game
    context_object_name = "games_list"
    template_name = "chess/save.html"

    from django.views.decorators.http import require_http_methods

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        game_time_white = 1000
        
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
    

    # If you are making a POST request, 'POST' must be in this list

    # @require_http_methods(["POST"])
    # def vote(request, pk):
        
    #     if request.method == 'POST':
    #         HttpResponse("POST request received")
    #         # Handle post
    #         pass

        # pk = 1
        # try:
        #     game = Game.objects.get(pk=game_id)
        #     print(game)
        # except Game.DoesNotExist:
        #     raise Http404("Game does not exist")
        # else:
        #     # Update the game instance with new data (example: updating game_time)
        #     game.game_time = 123  # Replace with actual data you want to save
        #     game.save()  # Save the updated instance to the database
        #     return redirect('chess:index', pk=game_id)  # Redirect to a success page or another view
        # return HttpResponseRedirect(reverse("chess:index.html", args=(game_id,)))
        # game = get_object_or_404(Game, pk=game_id)
        # print(game)
        # # try:
        # selected_choice = game.get(pk=request.POST["10"])

        # except (KeyError, Choice.DoesNotExist):
        #     # Redisplay the question voting form.
        #     return render(
        #         request,
        #         "chess/save.html",
        #         {
        #             "question": question,
        #             "error_message": "You didn't select a choice.",
        #         },
        #     )
        # else:
        #     selected_choice.votes = F("votes") + 1
        #     selected_choice.save()
        #     # Always return an HttpResponseRedirect after successfully dealing
        #     # with POST data. This prevents data from being posted twice if a
        #     # user hits the Back button.
        #     return HttpResponseRedirect(reverse("chess:index", args=(question.id,)))

# class IndexView(generic.ListView):
#     template_name = "chess/index.html"
#     context_object_name = "latest_question_list"

#     def get_queryset(self):
#         """
#         Return the last five published questions (not including those set to be
#         published in the future).
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
#             :5
#         ]

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = "chess/detail.html"

#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())

# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = "chess/results.html"

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(
#             request,
#             "chess/detail.html",
#             {
#                 "question": question,
#                 "error_message": "You didn't select a choice.",
#             },
#         )
#     else:
#         selected_choice.votes = F("votes") + 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse("chess:results", args=(question.id,)))