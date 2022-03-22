from rest_framework import serializers
from .models import Features, FeaturesCode


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = '__all__'

class FeaturesCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturesCode
        fields = '__all__'
