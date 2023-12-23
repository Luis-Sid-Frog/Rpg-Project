from django.urls import path
from .views import pages, crud, chapters


urlpatterns = [
    path('', pages.home, name='home'),
    path('game_scenerio/<str:pk>/', pages.game_scenerio_page, name='game_scenerio'),
    path('game_scenario/<int:game_scenario_id>/chapter', chapters.create, name='chapters_create'),
    path('createscenerio/', crud.create_scenerio, name='create-scenerio'),
    path('updatecenerio/<str:pk>/', crud.update_game_scenerio, name='update-scenerio'),
    path('deletecenerio/<str:pk>/', crud.delete_game_scenerio, name='delete-scenerio'),
    path('gamesystem/<str:pk>/', pages.game_system_page, name='game-system-page'),


]
