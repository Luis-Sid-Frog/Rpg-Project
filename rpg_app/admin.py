from django.contrib import admin
from .models import GameSystem


# Register your models here.

class GameSystemAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


admin.site.register(GameSystem, GameSystemAdmin)
