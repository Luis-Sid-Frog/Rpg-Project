from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from rpg_project.rpg_app.models import GameSystem, GameScenerio, Chapter, Comment, Character
from rpg_app.forms import GameScenerioForm

def create_scenerio(request):
    form = GameScenerioForm()
    if request.method == "POST":
        form = GameScenerioForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            game_scenario = form.save()
            return redirect('update-scenerio', pk=game_scenario.pk)
        else:
            print('not working')
    context = {'form': form, 'game_scenario': None}
    return render(request, 'game_scenario/scenario_form.html', context)


@login_required
def update_game_scenerio(request, pk):
    game_scenario = GameScenerio.objects.get(id=pk)
    if not game_scenario.is_author(request.user):
        raise PermissionDenied()

    chapters = Chapter.objects.filter(game_scenario_id=pk)
    characters = Character.objects.filter(game_scenario_id=pk)

    form = GameScenerioForm(instance=game_scenario)
    if request.method == "POST":
        form = GameScenerioForm(request.POST, instance=game_scenario)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form': form, 'game_scenario': game_scenario, 'chapters':chapters, 'characters':characters}
    return render(request, 'game_scenario/scenario_form.html', context)


def delete_game_scenerio(request, pk):
    game_scenerio = GameScenerio.objects.get(id=pk)
    if request.method == "POST":
        game_scenerio.delete()
        return redirect('home')
    context = {'obj': game_scenerio}
    return render(request, 'pages/../../templates/game_scenario/delete_scenario.html', context)

