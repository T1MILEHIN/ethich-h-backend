from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UniversalFormInput
from the_api.models import paymentStatus
from .serializers import UniversalFormInputSerializer
from the_api.serializers import paymentStatusSerialiizer
from django.utils import timezone

class AccessDataView(APIView):
    def get(self, request, unique_link):
        form_input = get_object_or_404(UniversalFormInput, unique_link=unique_link)
        serializer = UniversalFormInputSerializer(form_input)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PaymentConfirmationView(viewsets.ModelViewSet):
    queryset = paymentStatus.objects.all()
    serializer_class = paymentStatusSerialiizer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if not instance.payment_status:
            instance.payment_status = True
            instance.payment_date = timezone.now()
            instance.save()

            # Create form input data and generate a unique link
            form_input = UniversalFormInput.objects.create(users=instance.user, **request.data)
            unique_link = form_input.get_absolute_url()

            return Response({
                "message": "Payment confirmed and form data saved.",
                "unique_link": request.build_absolute_uri(unique_link)
            }, status=status.HTTP_200_OK)
        
        return Response({"message": "Payment has already been confirmed."}, status=status.HTTP_400_BAD_REQUEST)
    
class UniversalFormInputViewSet(viewsets.ModelViewSet):
    queryset = UniversalFormInput.objects.all()
    serializer_class = UniversalFormInputSerializer

    def create(self, request, *args, **kwargs):
        # Check if the user has made a payment
        if not paymentStatus.objects.filter(user=request.user, payment_status=True).exists():
            return Response({"details": "Payment is required to access this resource."}, status=status.HTTP_403_FORBIDDEN)
        
        return super().create(request, *args, **kwargs)
