from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models

from explorer.models import TimeStampModel


class SmartContract(TimeStampModel):
    """
    * name -> Smart Contract name | String | Required
    * compiled_version -> the solidity version used | String | Required
    * optimization -> if smart contract was optimized | Boolean | Required
    * source_code -> Smart Contract source code | Text | Required
    * address_hash -> Address Foreign key | ForeignKey | Required
    * abi -> Application Binary Interface | ArrayField | Required
    """

    name = models.CharField(
        max_length=255
    )
    compiled_version = models.CharField(
        max_length=50
    )
    optimization = models.BooleanField()
    source_code = models.TextField()
    address_hash = models.ForeignKey(
        'address.Address'
    )
    abi = ArrayField(
        JSONField()
    )
