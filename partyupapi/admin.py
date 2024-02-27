from django.contrib import admin
from .models import Games, User, LFGPost

admin.site.register(Games)
admin.site.register(User)
admin.site.register(LFGPost)
