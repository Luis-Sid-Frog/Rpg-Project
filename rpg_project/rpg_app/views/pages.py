from django.shortcuts import render, redirect
from rpg_project.rpg_app.models import GameSystem, GameScenerio, Comment
from django. contrib import messages

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    game_scenerios = GameScenerio.objects.filter(game_system__name__icontains=q)
    game_systems = GameSystem.objects.all()
    comments = Comment.objects.all().order_by('-created')
    context = {'game_scenerios': game_scenerios, 'game_systems':game_systems, 'comments':comments}
    return render(request, 'pages/home.html', context)


def game_scenerio_page(request, pk):
    game_scenerio = GameScenerio.objects.get(id=pk)
    comments = Comment.objects.all().order_by('-created')

    if request.method =='POST':
        comment = Comment.objects.create(
            author = request.user,
            game_scenerio = game_scenerio,
            comment_body= request.POST.get('comment_body'),
        )
        return redirect('game_scenerio', pk=game_scenerio.id)

    context = {'game_scenerio': game_scenerio, 'comments': comments}
    return render(request, 'pages/gameScenerio.html', context)
