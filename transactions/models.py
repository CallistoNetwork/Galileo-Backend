from django.db import models

from explorer.models import TimeStampModel


class Transaction(TimeStampModel):
    """
    * block_hash -> Block in which transaction was mined/validated. Can be null
    if is pending or only collated into one of the uncles. | Foreign Key
    * block_number -> Number block in which transaction was mined | Int ???
    * created_contract_address_hash -> Address ForeignKey only populated if
    to_address_hash is null
    * cumulative_gas_used -> Gas used in transaction block before transactions
    index, is None when transaction is pending | Decimal
    * error -> Error from the last Internal Transaction, Only set after
    `internal_transaction_index_at` is set AND if there was an error. | String
    * from_address_hash -> From Address transaction | Foreign Key
    * gas -> Gas provider by the sender | Decimal
    * gas_price -> How much the sender is willing to pay for the gas | Decimal
    * gas_used -> Gas used for just transaction, can be None when transaction
    is pending or has only been collated into one of the uncles in one of the
    Forks
    * hash -> Transaction hash | String
    * index -> transaction index in the Block can be None if transaction is
    pending or has only been collated into one of the uncles in one of the
    forks
    * input -> Data send with the transaction | String
    * internal_transactions_indexed_at -> When internal transactions were
    fetched by Indexer | Timestamp
    * nonce -> the number of transaction made by the sender prior to this one
    | Positive Int
    * r -> the R field ot fhe signature, r,s is the normal outpit of an ECDSA
    signature, where r is computed as the C coordinate of a point R, module the
    curve order n | Decimal
    * s -> the S field ot fhe signature, r,s is the normal outpit of an ECDSA
    signature, where r is computed as the C coordinate of a point R, module the
    curve order n | Decimal
    * status -> whether the transaction was successfully mined or failed. Can
    be None when transaction is pending or has only been collated into one of
    the uncles in one of the forks | String
    * to_address_hash -> To Address transaction | Foreign Key
    * v -> The V field of signature | String
    * value -> Wei transferred from `from_address` to `to_address`
    """

    block_hash = models.ForeignKey(
        'blocks.Block',
        on_delete=models.CASCADE,
        null=True
    )


class Fork(TimeStampModel):
    """
    A transaction fork has the same `hash` as a Transaction but associates that
    `hash` with a non-consensus uncle Block instead of the consensus block
    linked in the Transaction block_hash
    --Fields--
    * hash -> hash of contents of this transaction | String
    * index -> Index of this transaction in `uncle` Block | Int
    * transaction -> Data shared between all forks and the consensus
    transaction | Foreign Key
    * uncle_has -> uncle Block in which this transaction was mined/validated
    """


class InternalTransaction(TimeStampModel):
    """
    * call_type -> Type of call, None when type is not `call` | String
    * created_contract_code -> The code of the contract that was created when
    `call_type` is created | Text
    * created_contract_address_hash -> Address Foreign Key when Address is of
    a contract | Foreign Key
    * error -> error messages when call or create `call_type` | String
    * from_address_hash -> From Address Foreign Key | Foreign Key
    * gas -> the amount of gas allowed | Decimal
    * gas_used -> the amount of gas used, can be None when a call errors
    | Decimal
    * index -> Index of this transaction inside the Transaction | Int
    * init -> Constructor arguments for created_contract_code when `call_type`
    is created | Text
    * input -> input bytes to the call | Text
    * output -> output bytes from the call, can be None when a call errors
    | Text
    * to_address_hash -> To Address Foreign Key | Foreign Key
    * trace_address -> List of traces | Array of Int
    * transaction_hash -> Transaction in which this transaction occurred
    | Foreign Key
    * type -> Type of transaction `call`, `create`, `reward`, `suicide`
    | String
    * value -> value transferred from `from_address` to `to_address` | Decimal
    """
