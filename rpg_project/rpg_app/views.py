from django.shortcuts import render
from .models import GameSystem, GameScenerio


def home(request):
    game_scenerios = GameScenerio.objects.all()
    context = {'game_scenerios': game_scenerios}
    return render(request, 'pages/home.html', context)


def login(request):
    pass


def register(request):
    pass


def user_profile(request):
    pass


def game_system_page(request, pk):
    game_scenerio = GameScenerio.objects.get(id=pk)
    context = {'game_scenerio': game_scenerio}
    return render(request, 'pages/gameScenerio.html', context)

def scenerio_page(request):
    pass


def write_scenerio(request):
    pass
