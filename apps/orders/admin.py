from django.contrib import admin
from .models import OrderGroup, Order

class OrderInline(admin.TabularInline):
    model = Order
    extra = 0  # No extra empty forms
    readonly_fields = ('subtotal', 'product_name', 'product_price', 'product_category', 'product_stock', 'product_description')
    fields = ('product', 'quantity', 'subtotal', 'product_name', 'product_price', 'product_category', 'product_stock', 'product_description')
    
    def product_name(self, obj):
        return obj.product.name
    product_name.short_description = 'Mahsulot nomi'

    def product_price(self, obj):
        return f"{obj.product.price:.2f} so'm"
    product_price.short_description = 'Narxi'

    def product_category(self, obj):
        return obj.product.category_name
    product_category.short_description = 'Kategoriya'

    def product_stock(self, obj):
        return obj.product.stock
    product_stock.short_description = 'Zaxira'

    def product_description(self, obj):
        return obj.product.description or 'Tavsif mavjud emas'
    product_description.short_description = 'Tavsif'

    def subtotal(self, obj):
        return f"{obj.subtotal:.2f} so'm"
    subtotal.short_description = 'Jami narx'

@admin.register(OrderGroup)
class OrderGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'bot_user_chat_id', 'bot_user_name', 'bot_user_phone', 'total_price_display', 'is_paid', 'status', 'created_at')
    list_filter = ('status', 'is_paid', 'bot_user__platform')
    search_fields = ('bot_user__chat_id', 'bot_user__username', 'bot_user__phone_number')
    inlines = [OrderInline]
    readonly_fields = ('total_price_display', 'bot_user_chat_id', 'bot_user_name', 'bot_user_phone', 'bot_user_username', 'bot_user_platform', 'bot_user_profile_photo')

    def bot_user_chat_id(self, obj):
        return obj.bot_user.chat_id
    bot_user_chat_id.short_description = 'Chat ID'

    def bot_user_name(self, obj):
        full_name = f"{obj.bot_user.first_name or ''} {obj.bot_user.last_name or ''}".strip()
        return full_name or 'Ism mavjud emas'
    bot_user_name.short_description = 'Ism'

    def bot_user_phone(self, obj):
        return obj.bot_user.phone_number or 'Telefon raqami mavjud emas'
    bot_user_phone.short_description = 'Telefon'

    def bot_user_username(self, obj):
        return obj.bot_user.username or 'Username mavjud emas'
    bot_user_username.short_description = 'Username'

    def bot_user_platform(self, obj):
        return obj.bot_user.get_platform_display()
    bot_user_platform.short_description = 'Platforma'

    def bot_user_profile_photo(self, obj):
        return obj.bot_user.profile_photo_url or 'Rasm mavjud emas'
    bot_user_profile_photo.short_description = 'Profil rasmi'

    def total_price_display(self, obj):
        return f"{obj.total_price:.2f} so'm"
    total_price_display.short_description = 'Umumiy narx'