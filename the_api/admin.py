from django.contrib import admin
from .models import paymentStatus, PaymentPlan

# Register your models here.


class paymentStatusAdmin(admin.ModelAdmin):	
    list_display = ('user', 'name', 'email', 'phone_number', 'payment_status', 'payment_date', 'payment_plan')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('payment_status', 'payment_date')
    ordering = ('-payment_date','payment_status')
    
admin.site.register(paymentStatus, paymentStatusAdmin)


class PaymentPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan_type', 'start_date', 'end_date')
    search_fields = ('user__username',)
    list_filter = ('plan_type',)
    ordering = ('-start_date', 'end_date')
    
admin.site.register(PaymentPlan, PaymentPlanAdmin)    