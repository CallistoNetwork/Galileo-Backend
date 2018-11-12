from django.db import models

from explorer.models import TimeStampModel


class MarketHistory(TimeStampModel):
    """
    Record values of currency to USD for a single day

    date = The date
    opening_price -> Opening price
    closing_price -> Closing price
    """

    date = models.DateField()
    opening_price = models.DecimalField(
        max_digits=120,
        decimal_places=100
    )
    closing_price = models.DecimalField(
        max_digits=120,
        decimal_places=100
    )
