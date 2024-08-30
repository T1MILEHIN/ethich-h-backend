from rest_framework import serializers
from .models import UniversalFormInput

# Serializing the UniversalFormInput
class UniversalFormInputSerializer(serializers.ModelSerializer):  
    class Meta:
        model = UniversalFormInput
        fields = "__all__"
