from django.conf import settings
from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class paymentStatus(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    payment_status = models.BooleanField(default=False)
    payment_date = models.DateField(null=True, blank=True)
    
    
    def __str__(self):
        return f"PaymentStatus for: {self.user.username}"
    
    
    class Meta:
        verbose_name = "Payment Status"
        verbose_name_plural = "Payment Statuses"
