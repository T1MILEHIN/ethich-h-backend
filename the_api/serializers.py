from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from account.models import USERS
from the_api.models import paymentStatus

from django.utils import timezone


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
    
    
    
class paymentStatusSerialiizer(serializers.ModelSerializer):
    class Meta:
        model = paymentStatus
        fields = ("user","name", "email", "phone_number", "payment_status", "payment_date")
       

    def validate_payment_date(self, value):
       
        if value > timezone.now().date():
            raise serializers.ValidationError("Payment date cannot be in the future.")
        return value

