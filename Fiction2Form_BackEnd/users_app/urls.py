from django.urls import path, include
from .views import register_user

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# User URL Patterns
urlpatterns = [
    path('register/', register_user, name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
