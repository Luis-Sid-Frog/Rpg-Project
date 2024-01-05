from django.shortcuts import render, redirect
from rpg_project.rpg_app.models import Chapter
from rpg_project.rpg_app.forms import ChapterForm
from django.http import HttpResponseRedirect


def create(request, game_scenario_id):
    chapters = Chapter.objects.all()
    form = ChapterForm()
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    context = {'form': form, 'chapters':chapters}
    return render(request, 'chapters/create.html', context)
