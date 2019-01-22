from django.db import models

from explorer.models import TimeStampModel


class Token(TimeStampModel):
    """
    * name -> Name of token | String | optional
    * symbol -> Trading symbol | String | optional
    * total_supply -> The total supply if the token | Decimal | optional
    * decimals -> Number of decimal place the token can be subdivided to | Int
    | optional
    * type -> type of Token | String | required
    * cataloged -> if token information has been cataloged | Boolean | optional
    * contract_address_hash -> Foreign key to address | ForeignKey | required
    """

    name = models.CharField(
        max_length=255,
        blank=True
    )
    symbol = models.CharField(
        max_length=50,
        blank=True
    )
    total_supply = models.DecimalField(
        null=True,
        max_digits=120,
        decimal_places=18
    )
    decimals = models.PositiveIntegerField(
        null=True
    )
    token_type = models.CharField(
        max_length=100,
    )
    cataloged = models.BooleanField(
        null=True
    )
    contract_address_hash = models.ForeignKey(
        'address.Address',
        on_delete=models.PROTECT
    )


class TokenTransfer(TimeStampModel):
    """
    * amount -> token transfer amount | Decimal | Optional
    * from_address_hash -> Address send token | Foreign Key | Required
    * to_address_hash -> Address received token | Foreign Key | Required
    * token_contract_address_hash -> Address of the token contract
    | Forreign Key | Required
    * token_id -> Id of the token, only ERC-721 tokens | Optional
    * transaction_hash -> Transaction token | Foreign Key | Required
    * log_index -> Index of the corresponding Log in the transaction
    | Positive Int | Required
    """

    amount = models.DecimalField(
        null=True,
        max_digits=120,
        decimal_places=18
    )
    from_address_hash = models.ForeignKey(
        'address.Address',
        on_delete=models.PROTECT,
        related_name='token_transfer_from_address'
    )
    to_address_hash = models.ForeignKey(
        'address.Address',
        on_delete=models.PROTECT,
        related_name='token_transfer_to_address'
    )
    token_contract_address_hash = models.ForeignKey(
        'address.Address',
        on_delete=models.PROTECT,
        related_name='token_contract_address'
    )
    token_id = models.PositiveIntegerField(
        null=True
    )
    transaction_hash = models.ForeignKey(
        'transactions.Transaction',
        on_delete=models.PROTECT
    )
    log_index = models.PositiveIntegerField()
