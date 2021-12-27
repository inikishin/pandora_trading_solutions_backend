from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import MLModel, Horizon, Prediction, FitResults
from .serializers import MLModelSerializer, HorizonSerializer, PredictionSerializer, FitResultsSerializer


class MLModelViewSet(viewsets.ModelViewSet):
    queryset = MLModel.objects.all()
    serializer_class = MLModelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['external_id']


class HorizonViewSet(viewsets.ModelViewSet):
    queryset = Horizon.objects.all()
    serializer_class = HorizonSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['external_id']


class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['external_id']


class FitResultsViewSet(viewsets.ModelViewSet):
    queryset = FitResults.objects.all()
    serializer_class = FitResultsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['external_id']
