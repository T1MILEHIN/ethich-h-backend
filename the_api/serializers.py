from rest_framework.serializers import ModelSerializer
from account.models import USERS


class USER_REGISTRATION(ModelSerializer):
    class Meta:
        model = USERS
        # fields = ('username', 'firstname', 'lastname', 'email', 'password', 'is_staff')
        fields = "__all__"
        # extra_kwargs = {
        #     "password": {"write_only": True},
        # }

