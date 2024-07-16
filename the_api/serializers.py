from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from account.models import USERS


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

