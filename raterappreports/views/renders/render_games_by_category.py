from raterappreports.views import games_by_category
from django.shortcuts import render

def render_games_by_category(request):
    template = "games_by_category.html"

    context = {
        "category_games_list": games_by_category(request)
    }

    return render(request, template, context)