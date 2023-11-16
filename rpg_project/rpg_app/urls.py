from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('gamesystem/', views.game_system_page, name='game_system_page'),
]
