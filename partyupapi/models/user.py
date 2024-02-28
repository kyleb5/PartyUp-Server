from django.db import models

# Using Unique to prevent duplicates


class User(models.Model):
    fbKey = models.CharField(max_length=30)
    username = models.CharField(max_length=50, unique=True, default="username")
    email_address = models.EmailField(default="email")
    joinDate = models.DateTimeField(auto_now_add=True)
    account_playstation = models.CharField(max_length=50)
    account_xbox = models.CharField(max_length=50)
    account_steam = models.CharField(max_length=50)
    account_discord = models.CharField(max_length=50)
