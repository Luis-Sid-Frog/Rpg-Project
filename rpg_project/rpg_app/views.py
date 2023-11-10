from django.shortcuts import render

# Create your views here.


def home(request):
    pass


def login(request):
    pass


def register(request):
    pass


def user_profile(request):
    pass


def game_system_page(request):
    return render(request, 'pages/gameSystem.html')

def scenerio_page(request):
    pass


def write_scenerio(request):
    pass
