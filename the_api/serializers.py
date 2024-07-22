from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from account.models import USERS
from the_api.models import paymentStatus, PaymentPlan

from django.utils import timezone


# create a payment plan serializer
    
class PaymentPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentPlan
        fields = ["user", "plan_type", "start_date", "end_date",]
        
        

class USER_REGISTRATION(ModelSerializer):
    class Meta:
        model = USERS
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
        }
    def validate_email(self, value):
        if USERS.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use. Please use a different email.")
        return value

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    # create paymentstatus serializer
    
class paymentStatusSerialiizer(serializers.ModelSerializer):
    payment_plan = PaymentPlanSerializer()
    
    class Meta:
        model = paymentStatus
        fields = ("user","name", "email", "phone_number", "payment_status", "payment_date", "payment_plan")
       

    def validate_payment_date(self, value):
       
        if value > timezone.now().date():
            raise serializers.ValidationError("Payment date cannot be in the future.")
        return value
    
    def validate_payment_plan(self, validated_data):
        payment_plan_data = validated_data.pop("payment_plan")
        payment_status_instance = paymentStatus.objects.create(**validated_data)
        payment_plan_data.objects.create(payment_status=payment_status_instance, **payment_plan_data)
        
        return payment_status_instance
    
    
    
    
    
    
        

