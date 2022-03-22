from django.contrib import admin
from .models import MarketType, Market, Timeframe, Ticker, Quote, Currency, StockExchange


class TickerAdmin(admin.ModelAdmin):
    list_display = ['code', 'fullname', 'market']
    ordering = ['code']
    list_filter = ['market']


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['ticker', 'timeframe', 'datetime', 'open', 'high', 'low', 'close']
    ordering = ['ticker', 'datetime']
    list_filter = ['ticker']


admin.site.register(MarketType)
admin.site.register(StockExchange)
admin.site.register(Market)
admin.site.register(Timeframe)
admin.site.register(Ticker, TickerAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Currency)
