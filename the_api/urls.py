from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenBlacklistView  
)
from .views import usercreation, USERCREATION, MyTokenObtainPairView,paymentStatusView,paymentPlanView
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'payment-status', paymentStatusView)
router.register(r'payment-plan', paymentPlanView)


urlpatterns = [
    # path('register/', USERCREATION.as_view()),
    path('register/', usercreation),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    
    path('', include(router.urls)),
]
