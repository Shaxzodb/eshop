from django.urls import path, include
from .views import UserListCreateView
from rest_framework.routers import DefaultRouter
from .views import BotUserViewSet

router = DefaultRouter()
router.register('', BotUserViewSet)


urlpatterns = [
    path('admin-user', UserListCreateView.as_view(), name='user-list-create'),
    path('bot-users', include(router.urls)),
]

