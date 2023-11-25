from django.shortcuts import render, redirect
from rpg_project.rpg_app.models import GameSystem, GameScenerio, Comment
from rpg_app.forms import GameScenerioForm

def create_scenerio(request):
    form = GameScenerioForm()
    if request.method == "POST":
        form = GameScenerioForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
        else:
            print('not working')
    context = {'form': form}
    return render(request, 'pages/scenerio_form.html', context)


def update_game_scenerio(request, pk):
    game_scenerio = GameScenerio.objects.get(id=pk)
    form = GameScenerioForm(instance=game_scenerio)
    if request.method == "POST":
        form = GameScenerioForm(request.POST, instance=game_scenerio)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'pages/scenerio_form.html', context)


def delete_game_scenerio(request, pk):
    game_scenerio = GameScenerio.objects.get(id=pk)
    if request.method == "POST":
        game_scenerio.delete()
        return redirect('home')
    context = {'obj': game_scenerio}
    return render(request, 'pages/delete_scenerio.html', context)

