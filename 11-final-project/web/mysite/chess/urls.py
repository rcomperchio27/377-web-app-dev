from django.urls import path

from . import views

app_name = "chess"
urlpatterns = [
    path("<int:pk>/", views.GameIndexView.as_view(), name="index"),
    path("<int:pk>/detail/", views.UserDetailView.as_view(), name="detail"),
    path("<int:pk>/save/", views.GameResultsView.as_view(), name="save"),
    path("<int:pk>/login/", views.UserLoginView.as_view(), name="login"),
    path("login/", views.UserLoginView.as_view(), name="login"),
]