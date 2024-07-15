from rest_framework.serializers import ModelSerializer
from account.models import USERS


class USER_REGISTRATION(ModelSerializer):
    class Meta:
        model = USERS
        fields = "__all__"

