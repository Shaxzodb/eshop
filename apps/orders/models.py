from django.db import models

class OrderGroup(models.Model):
    STATUS_CHOICES = (
        ('active', 'Faol'),
        ('delivered', 'Yetkazib berilgan'),
        ('cancelled', 'Bekor qilingan'),
    )

    bot_user = models.ForeignKey('users.BotUser', on_delete=models.CASCADE, related_name="order_groups")
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
    )

    def __str__(self):
        return f"OrderGroup {self.id} for {self.bot_user.chat_id} ({self.status})"

    @property
    def total_price(self):
        """Calculate total price of all orders in this group"""
        return sum(order.subtotal for order in self.orders.all())

class Order(models.Model):
    order_group = models.ForeignKey(OrderGroup, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_group.bot_user.chat_id} - {self.product.name} ({self.quantity})"

    @property
    def subtotal(self):
        """Calculate subtotal for this order item"""
        return self.quantity * self.product.price