from django.db import models


class Games(models.Model):
    name = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='images/')
