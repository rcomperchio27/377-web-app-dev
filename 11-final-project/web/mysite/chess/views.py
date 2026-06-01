from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Choice, Question, Game, User
from django.http import Http404
from django.shortcuts import get_object_or_404, render
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
    
# class GameResultsView(generic.DetailView):
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