# apps/orders/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, MyOrderedProductsAPIView, OrderListView

router = DefaultRouter()
router.register('', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user-orders', MyOrderedProductsAPIView.as_view(), name='user-orders'),
    path('list', OrderListView.as_view(), name='order-list'),
]
