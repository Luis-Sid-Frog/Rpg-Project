from django.shortcuts import render, redirect
from rpg_project.rpg_app.models import GameSystem, GameScenerio, Comment
from django.contrib import messages
from rpg_project.users.models import User


def user_page(request, scenario_author):
    return render(request, 'users/user_detail.html')
