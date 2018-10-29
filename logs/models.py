from django.db import models

from explorer.models import TimeStampModel


class Log(TimeStampModel):
    """
    address_hash -> Address Foreign Key | Foreign Key
    data -> Not indexed log parameters | String
    first_topic -> topics[0] | String
    second_topic -> topics[1] | String
    third_topic -> topics[2] | String
    fourth_topic -> topics[3] | String
    index -> index of the log entry in all logs for the transaction | Int
    type -> type of event (parity only) | String
    transaction_hash -> parent Transaction of this log | Foreign Key
    """

    address_hash = models.ForeignKey(
        'address.Address',
        on_delete=models.PROTECT
    )
    data = models.TextField()
    first_topic = models.CharField(
        max_length=255
    )
    second_topic = models.CharField(
        max_length=255
    )
    third_topic = models.CharField(
        max_length=255
    )
    fourth_topic = models.CharField(
        max_length=255
    )
    index = models.PositiveIntegerField()
    event_type = models.CharField(
        max_length=255
    ),
    transaction_hash = models.ForeignKey(
        'transactions.Transaction'
    )
