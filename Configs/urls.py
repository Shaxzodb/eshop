from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Eshop API",
        default_version='v1',
        description="Bu Eshop loyihasining DRF Swagger hujjati",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # <-- bu login/logout form beradi
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login uchun
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Access token yangilash
    path('api/users/', include('apps.users.urls')),  # foydalanuvchilar uchun
    path('api/products/', include('apps.products.urls')),  # maxsulotlar ruyxati uchun
    path('api/orders/', include('apps.orders.urls')),  # buyurmalr ruyxati uchun

    # Swagger va Redoc yo'llari
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # JSON schema:
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # YAML schema:
    path('swagger.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-yaml'),
]
# Configs/urls.py yoki asosiy urls.py
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

