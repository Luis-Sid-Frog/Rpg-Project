from django.shortcuts import render
from rpg_project.rpg_app.models import GameSystem, GameScenerio, Comment


def home(request):
    game_scenerios = GameScenerio.objects.all()
    game_systems = GameSystem.objects.all()
    comments = Comment.objects.all()
    context = {'game_scenerios': game_scenerios, 'game_systems':game_systems, 'comments':comments}
    return render(request, 'pages/home.html', context)


def game_scenerio_page(request, pk):
    game_scenerio = GameScenerio.objects.get(id=pk)
    context = {'game_scenerio': game_scenerio}
    return render(request, 'pages/gameScenerio.html', context)
