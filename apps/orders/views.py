# apps/orders/views.py
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.products.serializers import ProductSerializer
from .models import OrderGroup, Order
from .serializers import OrderGroupSerializer, OrderSerializer
from .permissions import IsAdminOrOwnerOnly

class OrderGroupViewSet(viewsets.ModelViewSet):
    queryset = OrderGroup.objects.all().select_related('bot_user').prefetch_related('orders')
    serializer_class = OrderGroupSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        chat_id = self.request.query_params.get('chat_id')
        status = self.request.query_params.get('status')

        queryset = self.queryset
        
        if user and user.is_staff:
            if status:
                queryset = queryset.filter(status=status)
            return queryset
        
        if chat_id:
            queryset = queryset.filter(bot_user__chat_id=chat_id)
            if status:
                queryset = queryset.filter(status=status)
            return queryset
        
        return OrderGroup.objects.none()

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().select_related('order_group', 'product', 'order_group__bot_user')
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        chat_id = self.request.query_params.get('chat_id')
        status = self.request.query_params.get('status')

        queryset = self.queryset
        
        if user and user.is_staff:
            if status:
                queryset = queryset.filter(order_group__status=status)
            return queryset
        
        if chat_id:
            queryset = queryset.filter(order_group__bot_user__chat_id=chat_id)
            if status:
                queryset = queryset.filter(order_group__status=status)
            return queryset
        
        return Order.objects.none()

class MyOrderedProductsAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        chat_id = request.query_params.get('chat_id')
        if not chat_id:
            return Response({"detail": "chat_id kerak"}, status=400)

        orders = Order.objects.filter(order_group__bot_user__chat_id=chat_id)
        products = [order.product for order in orders]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class OrderGroupListView(generics.ListAPIView):
    serializer_class = OrderGroupSerializer

    def get_queryset(self):
        queryset = OrderGroup.objects.all()
        status = self.request.query_params.get('status')
        if status in ['active', 'delivered', 'cancelled']:
            queryset = queryset.filter(status=status)
        return queryset

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        status = self.request.query_params.get('status')
        if status in ['active', 'delivered', 'cancelled']:
            queryset = queryset.filter(order_group__status=status)
        return queryset