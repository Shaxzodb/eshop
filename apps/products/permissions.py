from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.permissions import SAFE_METHODS

# Custom permission (optional, agar tayyor `IsAdminUserOrReadOnly` ishlatmoqchi bo'lmasangiz)
from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Ruxsat: GET, HEAD, OPTIONS — hamma oladi.
    Boshqa amallar (POST, PUT, DELETE) — faqat admin foydalanuvchi.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
