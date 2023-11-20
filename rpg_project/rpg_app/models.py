from django.db import models
from django.conf import settings


# Create your models here.
class GameSystem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class GameScenerio(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game_system = models.ForeignKey(GameSystem, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField()
    characters = models.TextField(null=True)
    maps = models.ImageField( null=True)
    locations = models.ImageField(null=True)
    notes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game_scenerio = models.ForeignKey(GameScenerio, on_delete=models.CASCADE)
    comment_body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.comment_body[:50]}...'
