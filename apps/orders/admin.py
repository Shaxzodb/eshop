# apps/orders/admin.py

from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'bot_user', 'product', 'quantity', 'is_paid', 'status', 'created_at']
    list_filter = ['status', 'is_paid', 'created_at']
