# apps/orders/models.py

from django.db import models

class Order(models.Model):
    STATUS_CHOICES = (
        ('active', 'Faol'),
        ('delivered', 'Yetkazib berilgan'),
    )

    bot_user = models.ForeignKey('users.BotUser', on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
    )

    def __str__(self):
        return f"{self.bot_user.chat_id} - {self.product.name} ({self.status})"
    

