from django.urls import path
from .views import render_games_by_category

urlpatterns = [
    path("reports/games", render_games_by_category)
]