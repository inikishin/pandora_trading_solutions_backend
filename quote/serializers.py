from rest_framework import serializers
from .models import Market, MarketType, Timeframe, Ticker, Quote, Currency, StockExchange


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'


class MarketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketType
        fields = '__all__'


class TimeframeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeframe
        fields = '__all__'


class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = '__all__'


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class StockExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockExchange
        fields = '__all__'
