from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentConfirmationView, AccessDataView, UniversalFormInputViewSet

router = DefaultRouter()
router.register(r'universal-form-inputs', UniversalFormInputViewSet)
router.register(r'payment-confirmation', PaymentConfirmationView, basename='payment-confirmation')

urlpatterns = [
    path('access-data/<uuid:unique_link>/', AccessDataView.as_view(), name='access_data'),
    path('', include(router.urls)),
]
