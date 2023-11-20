from django.shortcuts import render
from rpg_project.rpg_app.models import GameSystem, GameScenerio, Comment
from rpg_app.forms import GameScenerioForm

def create_scenerio(request):
    form = GameScenerioForm()
    context = {'form': form}
    return render(request, 'pages/scenerio_form.html', context)
