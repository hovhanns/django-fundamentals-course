from django.shortcuts import render

from django.shortcuts import render
from gameplay.models import Game


def home(request):
    return render(request, "player/home.html",
                  {'ngames': Game.objects.count()})
