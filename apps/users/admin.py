from django.contrib import admin
from .models import User, BotUser

admin.site.register(User)
admin.site.register(BotUser)
