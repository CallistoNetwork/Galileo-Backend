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
    coin_balance = models.DecimalField(
        max_digits=120,
        decimal_places=0,
        blank=True,
        null=True
    )
    coin_balance_block = models.IntegerField(
        blank=True,
        null=True
    )


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
    * block_number -> Number of the block | Big Int
    * value -> Value of address at the end of the Block
    * value_fetched_at -> When value was fetched
    """

    address_hash = models.ForeignKey(
        'Address',
        on_delete=models.PROTECT
    )
    block_number = models.BigIntegerField()
    value = models.DecimalField(
        null=True,
        max_digits=120,
        decimal_places=0
    )
    value_fetched_at = models.DateTimeField(
        null=True
    )


class AddressTokenBalance(TimeStampModel):
    """
    * address_hash -> Foreign Key to Address | Foreign Key
    * block_number -> Number of the block | Big Int
    * token_contract_address_hash -> Foreign Key to Token | Foreign Key
    * value -> Value of address at the end of the Block
    * value_fetched_at -> When value was fetched
    """
    address_hash = models.ForeignKey(
        'Address',
        on_delete=models.CASCADE
    )
    block_number = models.BigIntegerField()
    token_contract_address_hash = models.ForeignKey(
        'tokens.Token',
        on_delete=models.CASCADE
    )
    value = models.DecimalField(
        null=True,
        max_digits=120,
        decimal_places=0
    )
    value_fetched_at = models.DateTimeField(
        null=True
    )

