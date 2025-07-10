# apps/orders/permissions.py

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrOwnerOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True
        return False  # DRF user bo‘lmagani uchun faqat admin uchun

    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True
        if request.method == 'POST':
            return True  # Botdan kelgan foydalanuvchilar buyurtma yaratishi mumkin
        return False
