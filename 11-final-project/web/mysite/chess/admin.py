from django.contrib import admin

from .models import Choice, Question
from .models import Game, User

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

class GameAdmin(admin.ModelAdmin):
    list_display = ["game_board", "user_id"]
    search_fields = ["game_board"]

class UserAdmin(admin.ModelAdmin):
    list_display = ["user_name", "user_games", "user_wins", "user_losses", "user_saved_game", "user_current_games"]
    list_filter = ["user_games"]
    search_fields = ["user_name"]

# admin.site.register(Question, QuestionAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(User, UserAdmin)