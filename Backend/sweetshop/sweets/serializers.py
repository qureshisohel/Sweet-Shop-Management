from rest_framework import serializers
from .models import Sweet

class SweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sweet
        fields = ['id', 'name', 'category', 'price', 'quantity']

class SweetSearchSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    category = serializers.CharField(required=False)
    min_price = serializers.DecimalField(required=False, max_digits=6, decimal_places=2)
    max_price = serializers.DecimalField(required=False, max_digits=6, decimal_places=2)