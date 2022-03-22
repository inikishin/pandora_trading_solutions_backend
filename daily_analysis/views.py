from datetime import datetime
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Features, FeaturesCode
from .serializers import FeaturesSerializer, FeaturesCodeSerializer


class FeaturesCodeViewSet(viewsets.ModelViewSet):
    queryset = FeaturesCode.objects.all()
    serializer_class = FeaturesCodeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['external_id']


class FeaturesViewSet(viewsets.ModelViewSet):
    queryset = Features.objects.all().order_by('datetime')
    serializer_class = FeaturesSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['external_id', 'ticker', 'datetime']

    @action(detail=False, methods=['GET'])
    def get_available_daily_analysis_posts(self, request):
        last_quotes = list(Features.objects.all().order_by('datetime').values('ticker', 'ticker__code', 'datetime'))

        return Response(last_quotes[-10:])

    @action(detail=False, methods=['GET'])
    def get_features_for_daily_analysis_post(self, request):
        ticker_id = request.query_params.get('ticker', None)
        on_date = request.query_params.get('on_date', None)

        if not ticker_id or not on_date:
            print('Exit. Ticker or Date not specified')
            return Response([])

        on_date = datetime.strptime(on_date, '%Y%m%d')
        print(on_date)
        last_quotes = list(Features.objects.filter(ticker=ticker_id, datetime__lte=on_date).order_by('datetime').values())

        return Response(last_quotes[-80:])

