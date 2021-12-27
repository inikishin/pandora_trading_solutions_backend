import uuid
from django.db import models


class Currency(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=1000, blank=True, null=True)
    external_id = models.CharField(max_length=255, unique=True)

    def __repr__(self):
        return f'{self.code} (id: {self.pk})'

    def __str__(self):
        return self.code


class Timeframe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=10, unique=True)
    external_id = models.CharField(max_length=255, unique=True)

    def __repr__(self):
        return f'{self.code} (id: {self.pk})'

    def __str__(self):
        return f'{self.code}'


class MarketType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    external_id = models.CharField(max_length=255, unique=True)

    def __repr__(self):
        return f'{self.code} (id: {self.pk})'

    def __str__(self):
        return self.code


class StockExchange(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    external_id = models.CharField(max_length=255, unique=True)

    def __repr__(self):
        return f'{self.code} (id: {self.pk})'

    def __str__(self):
        return self.code


class Market(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, null=True, blank=True)
    type = models.ForeignKey(MarketType, on_delete=models.CASCADE)
    stock_exchange = models.ForeignKey(StockExchange, on_delete=models.CASCADE)
    external_id = models.CharField(max_length=255, unique=True)

    # TODO add working hours and days
    def __repr__(self):
        return f'{self.code} (id: {self.pk})'

    def __str__(self):
        return self.code


class Ticker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, null=True, blank=True)
    site = models.CharField(max_length=500, null=True, blank=True)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    external_id = models.CharField(max_length=255, unique=True)

    models.UniqueConstraint(fields=['code', 'market'], name='unique_ticker_code_in_market')

    def __repr__(self):
        return f'{self.code} (id: {self.pk})'

    def __str__(self):
        return self.code


class Quote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    timeframe = models.ForeignKey(Timeframe, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()
    external_id = models.CharField(max_length=255, unique=True)

    models.UniqueConstraint(fields=['ticker', 'timeframe', 'datetime'],
                            name='unique_quote_for_ticker_timeframe_datetime')

    def __repr__(self):
        return f'{self.ticker} {self.timeframe} {self.datetime} (O: {self.open} H: {self.high} L: {self.low} C: {self.close})'

    def __str__(self):
        return f'{self.ticker} {self.timeframe} {self.datetime} (O: {self.open} H: {self.high} L: {self.low} C: {self.close})'
