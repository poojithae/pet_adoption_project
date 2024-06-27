from rest_framework import serializers
from .models import pet

class petSerializer(serializers.ModelSerializer):
    class Meta:
        model = pet
        fields = '__all__'
