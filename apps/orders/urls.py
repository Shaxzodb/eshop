from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.orders.views import OrderGroupViewSet, OrderViewSet, MyOrderedProductsAPIView, OrderListView

router = DefaultRouter()
router.register(r'order-groups', OrderGroupViewSet, basename='order-groups')
router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('my-ordered-products/', MyOrderedProductsAPIView.as_view(), name='my-ordered-products'),
    path('orders-list/', OrderListView.as_view(), name='order-list'),
    path('', include(router.urls)),
]