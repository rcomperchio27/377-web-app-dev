from django.urls import path

from . import views

app_name = "chess"
urlpatterns = [
    path("<int:pk>/", views.GameIndexView.as_view(), name="index"),
    path("<int:pk>/detail/", views.UserDetailView.as_view(), name="detail"),
    path("<int:pk>/save/", views.GameResultsView.as_view(), name="vote"),
    # path("<int:game_id>/save/", views.save.as_view(), name="save"),
]