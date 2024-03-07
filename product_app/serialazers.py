from  rest_framework import serializers
from .models import PRODUCT

class PRODUCTSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRODUCT
        fields = '__all__'
        