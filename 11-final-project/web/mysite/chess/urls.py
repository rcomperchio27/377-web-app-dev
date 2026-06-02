from django.urls import path

from . import views

app_name = "chess"
urlpatterns = [
    path("<int:pk>/", views.GameIndexView.as_view(), name="index"),
    path("<int:pk>/detail/", views.UserDetailView.as_view(), name="detail"),
    # path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # path("<int:game_id>/save/", views.save.as_view(), name="save"),
]