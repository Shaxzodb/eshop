from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSuperUser(permissions.BasePermission):
    """
    Faqat superuser foydalanuvchilarga ruxsat beradi.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsAdminUser(permissions.BasePermission):
    """
    Superuser yoki staff (admin) foydalanuvchilarga ruxsat beradi.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (
            request.user.is_superuser or request.user.is_staff
        ))


class IsStaffUser(permissions.BasePermission):
    """
    Faqat staff (admin) foydalanuvchilarga ruxsat beradi.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)


class ReadOnly(permissions.BasePermission):
    """
    Faqat o‘qish (GET, HEAD, OPTIONS) ruxsat beradi.
    """
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

class IsAdminOrCreateOnly(BasePermission):
    """
    Faqat admin foydalanuvchi GET, PUT, DELETE qilsin.
    Oddiy foydalanuvchi faqat POST (yaratish) qilishi mumkin.
    """

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True  # Har kim POST qila oladi (masalan, bot)
        return bool(request.user and request.user.is_staff)

