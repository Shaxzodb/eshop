from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username
    
class BotUser(models.Model):
    PLATFORM_CHOICES = (
        ('telegram', 'Telegram'),
        ('whatsapp', 'WhatsApp'),
    )

    chat_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)  # ✅
    profile_photo_url = models.URLField(blank=True, null=True)             # ✅
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, default='telegram')
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username or self.chat_id} ({self.platform})"
    

