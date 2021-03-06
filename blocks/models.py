from django.contrib.postgres.fields import BigIntegerRangeField
from django.db import models

from explorer.models import TimeStampModel


class Block(TimeStampModel):
    """
    * consensus -> | Boolean |
        * True = this is a block on the longest concensus agreed upon chain
        * False = this is an uncle block from a fork
    * difficulty -> How hard was mining the block | Decimal
    * gas_limit -> Gas limit for the block | Decimal
    * gas_used -> Current Gas used to mining or validate transactions in the
    blog | Decimal
    * hash -> Hash of the block | String
    * miner -> Address Foreign Key | Foreign Key |
    * nonce -> proof-of-work hash, not used in POA chains | String
    * number -> Block number in the chain | Int
    * parent_hash -> previous block self Foreign Key | Foreign Key |
    * size -> Block size in bytes | Integer
    * timestamp -> when block was collated | Timestamp
    * total_difficulty -> Total difficulty of the chain until this block
    | Decimal
    """
    consensus = models.BooleanField(
        null=True
    )
    difficulty = models.DecimalField(
        max_digits=120,
        decimal_places=0
    )
    gas_limit = models.DecimalField(
        max_digits=120,
        decimal_places=0
    )
    gas_used = models.DecimalField(
        max_digits=120,
        decimal_places=0
    )
    hash = models.CharField(
        max_length=255,
        unique=True
    )
    miner = models.ForeignKey(
        'address.Address',
        on_delete=models.PROTECT
    )
    nonce = models.CharField(
        max_length=255,
        blank=True
    )
    number = models.BigIntegerField()
    parent_hash = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        to_field='hash',
        null=True
    )
    size = models.IntegerField()
    timestamp = models.BigIntegerField()
    total_difficulty = models.DecimalField(
        max_digits=120,
        decimal_places=0
    )


class SecondDegreeRelation(TimeStampModel):
    """
    * nephew_hash -> Block Foreign key | Foreign key
    * uncle_hash -> Block Foreign Key | Foreign Key
    * uncle_fetched_at -> When Block for uncle_hash was confirmed has fetched
    | Timestamp
    """
    nephew_hash = models.ForeignKey(
        'Block',
        on_delete=models.PROTECT,
        related_name='nephew_block_relation'
    )
    uncle_hash = models.ForeignKey(
        'Block',
        on_delete=models.PROTECT,
        related_name='uncle_block_relation'
    )
    uncle_fetched_at = models.BigIntegerField()


class BlockReward(TimeStampModel):
    """
    Represents the static reward given to the miner of a block in a range of
    block numbers.

    block_range -> Range of the block numbers
    reward -> Reward given
    """

    block_range = BigIntegerRangeField()
    reward = models.DecimalField(
        max_digits=120,
        decimal_places=0
    )
