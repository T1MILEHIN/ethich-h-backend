from django.conf import settings
from django.db import models
# from django.contrib.auth.models import User



# create the payment plan model

class PaymentPlan(models.Model):
    WEEKLY = "W"
    MONTHLY = "M"
    YEARLY = "Y"
    
    plan_choices = [
        (WEEKLY, "Weekly"),
        (MONTHLY, "Monthly"),
        (YEARLY, "Yearly"),
    ]
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan_type = models.CharField(max_length=1, choices=plan_choices, default=WEEKLY)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Payment Plan: {self.get_plan_type_display()}"
    
    class Meta:
        verbose_name = "Payment Plan"
        verbose_name_plural = "Payment Plans"
    

# Create the payment status model.

class paymentStatus(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    payment_status = models.BooleanField(default=False)
    payment_date = models.DateField(null=True, blank=True)
    payment_plan = models.ForeignKey(PaymentPlan, on_delete=models.SET_NULL, null=True, blank=True)


    
    def __str__(self):
        return f"PaymentStatus for: {self.user.username}"
    
    
    class Meta:
        verbose_name = "Payment Status"
        verbose_name_plural = "Payment Statuses"


