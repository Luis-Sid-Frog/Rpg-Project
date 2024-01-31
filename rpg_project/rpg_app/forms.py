from django.forms import ModelForm
from rpg_project.rpg_app.models import GameScenerio, Chapter, Character


class GameScenerioForm(ModelForm):
    class Meta:
        model = GameScenerio
        fields = '__all__'
        exclude = ['author']


class ChapterForm(ModelForm):
    class Meta:
        model = Chapter
        fields = '__all__'


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = '__all__'
