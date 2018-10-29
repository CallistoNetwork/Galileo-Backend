from django.db import models

from explorer.models import TimeStampModel


class Address(TimeStampModel):
    """
    * hash -> hash address public key | String | Required
    * coin_balance -> Last fetched balance from parity | Wei (String)
    | Optional
    * coin_balance_block -> Block number which coin balance was fetched
    | ForeignKey | Optional
    """
    hash = models.CharField(
        max_length=255,
    )
    coin_balance = models.DecimalField()
    coin_balance_block = models.IntegerField()


class AddressName(TimeStampModel):
    """
    * address_hash -> Foreign key to Address Model | ForeignKey | Required
    * name -> Name for the address | String | Required
    * primary -> if the name is the primary name for the address | Boolean
    | Optional
    """

    address_hash = models.ForeignKey(
        'Address',
        on_delete=models.PROTECT
    )
    name = models.CharField(
        max_length=255
    )
    primary = models.BooleanField()


class AddressCoinBalance(TimeStampModel):
    """
    * address_hash -> Foreign Key to Address | Foreign Key
    * block_number -> Foreign Key to Block | Foreign Key
    * value -> Value of address at the end of the Block
    * value_fetched_at -> When value was fetched
    """

    address_hash = models.ForeignKey(
        'Address',
        on_delete=models.PROTECT
    )
    block_number = models.ForeignKey(
        'blocks.Block',
        on_delete=models.PROTECT
    )
    value = models.DecimalField(
        null=True
    )
    value_fetched_at = models.DateTimeField(
        null=True
    )


