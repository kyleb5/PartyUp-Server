from django.db import models

# Using Unique to prevent duplicates


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    fbKey = models.CharField(max_length=30)
    joinDate = models.IntegerField()
    account_playstation = models.CharField(max_length=50, unique=True)
    account_xbox = models.CharField(max_length=50, unique=True)
    account_steam = models.CharField(max_length=50, unique=True)
    account_discord = models.CharField(max_length=50, unique=True)
