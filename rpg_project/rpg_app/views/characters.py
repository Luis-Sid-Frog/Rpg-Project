from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from rpg_project.rpg_app.models import Character, GameScenerio
from rpg_project.rpg_app.forms import CharacterForm


def create(request, game_scenario_id):
    characters = Character.objects.all()
    game_scenario = GameScenerio.objects.get(id=game_scenario_id)
    form = CharacterForm()
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('update-scenerio', pk=game_scenario_id)
    context = {'form': form, 'characters': characters, 'game_scenario': game_scenario}
    return render(request, 'characters/create.html', context)


def update(request, game_scenario_id, character_id):
    character = Character.objects.get(id=character_id)
    characters = Character.objects.filter(game_scenario_id=game_scenario_id)
    form = CharacterForm(instance=character)
    game_scenario = GameScenerio.objects.get(id=game_scenario_id)
    if not game_scenario.is_author(request.user):
        raise PermissionDenied()

    if request.method == 'POST':
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            return redirect('update-scenerio', pk=game_scenario_id)
    context = {'form': form, 'character': character, 'characters': characters, 'game_scenario': game_scenario}
    return render(request, 'characters/create.html', context)
