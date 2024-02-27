from django.db import models
from .games import Games
from .user import User


class LFGPost(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    needed_players = models.IntegerField()
    skill_level = models.CharField(max_length=20)
    platform = models.TextField()
    region = models.TextField()
    mic_needed = models.BooleanField()
    status = models.BooleanField()
    uuid = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
