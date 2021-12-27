from rest_framework import serializers
from .models import MLModel, FitResults, Horizon, Prediction


class MLModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLModel
        fields = '__all__'


class FitResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitResults
        fields = '__all__'


class HorizonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horizon
        fields = '__all__'


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = '__all__'

