from django.forms import ModelForm
from rpg_project.rpg_app.models import GameScenerio


class GameScenerioForm(ModelForm):
    class Meta:
        model = GameScenerio
        fields = '__all__'
        exclude = ['author']
