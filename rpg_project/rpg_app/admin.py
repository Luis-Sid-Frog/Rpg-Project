from django.contrib import admin
from .models import GameSystem, GameScenerio, Comment


class GameSystemAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]

admin.site.register(GameSystem)
admin.site.register(GameScenerio)
admin.site.register(Comment)

