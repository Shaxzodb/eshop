# apps/orders/serializers.py

from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'bot_user', 'product', 'quantity', 'created_at', 'is_paid', 'status']

