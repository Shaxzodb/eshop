# apps/orders/views.py
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from apps.products.serializers import ProductSerializer
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from .permissions import IsAdminOrOwnerOnly

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrOwnerOnly]

    def get_queryset(self):
        user = self.request.user

        # 1. Admin barcha buyurtmalarni ko‘ra oladi
        if user and user.is_staff:
            return Order.objects.all()

        # 2. Oddiy foydalanuvchi: chat_id orqali filtering
        chat_id = self.request.query_params.get('chat_id')
        if chat_id:
            return Order.objects.filter(bot_user__chat_id=chat_id)

        # 3. Agar chat_id yo‘q bo‘lsa, hech narsa ko‘rsatmaydi
        return Order.objects.none()
    

class MyOrderedProductsAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        chat_id = request.query_params.get('chat_id')
        if not chat_id:
            return Response({"detail": "chat_id kerak"}, status=400)

        orders = Order.objects.filter(bot_user__chat_id=chat_id)
        products = [order.product for order in orders]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        status = self.request.query_params.get('status')
        if status in ['active', 'delivered']:
            queryset = queryset.filter(status=status)
        return queryset


