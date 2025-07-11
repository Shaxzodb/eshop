# orders/serializers.py
from rest_framework import serializers
from .models import OrderGroup, Order
from ..products.serializers import ProductSerializer
from ..products.models import Product

class OrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    subtotal = serializers.FloatField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order_group', 'product', 'quantity', 'subtotal', 'created_at']

class OrderGroupSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)
    total_price = serializers.FloatField(read_only=True)

    class Meta:
        model = OrderGroup
        fields = ['id', 'bot_user', 'created_at', 'is_paid', 'status', 'orders', 'total_price']