from django.db import models
from .user import User
from .lfg_post import LFGPost


class LFGGroupMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(LFGPost, on_delete=models.CASCADE)
