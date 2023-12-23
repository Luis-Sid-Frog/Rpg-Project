from django.shortcuts import render, redirect
from rpg_project.rpg_app.models import Chapter
from rpg_project.rpg_app.forms import ChapterForm


def create(request, game_scenario_id):
    form = ChapterForm()
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_scenario')
    return render(request, 'chapters/create.html')
