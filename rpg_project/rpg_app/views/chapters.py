from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from rpg_project.rpg_app.models import Chapter, GameScenerio
from rpg_project.rpg_app.forms import ChapterForm


def create(request, game_scenario_id):
    chapters = Chapter.objects.all()
    game_scenario = GameScenerio.objects.get(id=game_scenario_id)
    form = ChapterForm()
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('update-scenerio', pk=game_scenario_id)
    context = {'form': form, 'chapters': chapters, 'game_scenario': game_scenario}
    return render(request, 'chapters/create.html', context)


def update(request, game_scenario_id, chapter_id):
    chapter = Chapter.objects.get(id=chapter_id)
    chapters = Chapter.objects.filter(game_scenario_id=game_scenario_id)
    form = ChapterForm(instance=chapter)
    game_scenario = GameScenerio.objects.get(id=game_scenario_id)
    if not game_scenario.is_author(request.user):
        raise PermissionDenied()

    if request.method == 'POST':
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return redirect('update-scenerio', pk=game_scenario_id)
    context = {'form': form, 'chapter': chapter, 'chapters': chapters, 'game_scenario': game_scenario}
    return render(request, 'chapters/create.html', context)
