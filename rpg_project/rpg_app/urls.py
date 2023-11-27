from django.urls import path
from .views import pages, crud


urlpatterns = [
    path('', pages.home, name='home'),
    path('gamescenerio/<str:pk>/', pages.game_scenerio_page, name='game_scenerio'),
    path('createscenerio/', crud.create_scenerio, name='create-scenerio'),
    path('updatecenerio/<str:pk>/', crud.update_game_scenerio, name='update-scenerio'),
    path('deletecenerio/<str:pk>/', crud.delete_game_scenerio, name='delete-scenerio'),

]
