# apps/users/views.py
from rest_framework import generics, viewsets
from .models import User, BotUser
from .serializers import UserSerializer, BotUserSerializer
from .permissions import IsSuperUser, IsAdminOrCreateOnly  # bu yerda import qilamiz
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUser]  # faqat superadminlar ruxsat oladi

class BotUserViewSet(viewsets.ModelViewSet):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        chat_id = self.request.query_params.get('chat_id')
        if chat_id:
            return self.queryset.filter(chat_id=chat_id)
        return self.queryset
    def create(self, request, *args, **kwargs):
        data = request.data

        chat_id = data.get("chat_id")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        platform = data.get("platform")
        phone_number = data.get("phone_number")  # ✅ yangi maydon
        profile_photo_url = data.get("profile_photo_url")  # ✅ yangi maydon

        if not chat_id:
            return Response({"error": "chat_id kerak"}, status=400)

        bot_user, created = BotUser.objects.get_or_create(
            chat_id=chat_id,
            defaults={
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "platform": platform,
                "phone_number": phone_number,  # ✅ kiritamiz
                "profile_photo_url": profile_photo_url,  # ✅ kiritamiz
            }
        )

        serializer = self.get_serializer(bot_user)
        if not created:
            return Response({"detail": "Bu foydalanuvchi allaqachon mavjud", "user": serializer.data}, status=200)
        return Response(serializer.data, status=201)


