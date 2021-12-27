from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Features
from .serializers import FeaturesSerializer


class FeaturesViewSet(viewsets.ModelViewSet):
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['external_id']
