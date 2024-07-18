from django.contrib import admin
from .models import paymentStatus

# Register your models here.


class paymentStatusAdmin(admin.ModelAdmin):	
    list_display = ('user', 'name', 'email', 'phone_number', 'payment_status', 'payment_date')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('payment_status', 'payment_date')
    ordering = ('-payment_date','payment_status')
    
admin.site.register(paymentStatus, paymentStatusAdmin)