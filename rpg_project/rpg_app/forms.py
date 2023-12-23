from django.forms import ModelForm
from rpg_project.rpg_app.models import GameScenerio, Chapter


class GameScenerioForm(ModelForm):
    class Meta:
        model = GameScenerio
        fields = '__all__'
        exclude = ['author']


class ChapterForm(ModelForm):
    class Meta:
        model = Chapter
        fields = '__all__'
