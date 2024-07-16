from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenBlacklistView
)
from .views import usercreation, MyTokenObtainPairView

urlpatterns = [
    path('register/', usercreation),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
