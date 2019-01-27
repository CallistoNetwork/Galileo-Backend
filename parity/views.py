from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.urls import reverse
from django.views import View
from rest_framework.views import APIView

from web3 import Web3, WebsocketProvider

from .utils import web3_to_dict

from address.models import Address
from blocks.models import Block, SecondDegreeRelation
from transactions.models import Transaction, Fork

parity_url = settings.PARITY_NODE_URL
w3_client = Web3(WebsocketProvider(parity_url))


class SaveView(View):

    def get(self, request, *args, **kwargs):

        block_hash = kwargs['hash']

        block_info = w3_client.eth.getBlock(block_hash)

        block_data = web3_to_dict(block_info)

        miner = self.get_address(block_data['miner'])

        existing_block = Block.objects.filter(
            hash=block_data['hash']
        )

        if existing_block.exists():
            block = existing_block.first()
            block.difficulty = block_data['difficulty']
            block.gas_limit = block_data['gasLimit']
            block.gas_used = block_data['gasUsed']
            block.hash = block_data['hash']
            block.miner = miner
            block.nonce = block_data['nonce']
            block.number = block_data['number']
            block.parent_hash = Block.objects.filter(
                hash=block_data['parentHash']
            ).first()
            block.size = block_data['size']
            block.timestamp = block_data['timestamp']
            block.total_difficulty = block_data['totalDifficulty']
            block.save()
        else:
            # Create Block Instance
            block = Block()
            block.difficulty = block_data['difficulty']
            block.gas_limit = block_data['gasLimit']
            block.gas_used = block_data['gasUsed']
            block.hash = block_data['hash']
            block.miner = miner
            block.nonce = block_data['nonce']
            block.number = block_data['number']
            block.parent_hash = Block.objects.filter(
                hash=block_data['parentHash']
            ).first()
            block.size = block_data['size']
            block.timestamp = block_data['timestamp']
            block.total_difficulty = block_data['totalDifficulty']
            block.save()

        # Create transactions for block
        for transaction in block_data['transactions']:
            transaction_info = w3_client.eth.getTransaction(transaction)
            transaction_data = web3_to_dict(transaction_info)

            existing_transaction = Transaction.objects.filter(
                hash=transaction_data['hash']
            )

            if existing_transaction.exists():
                transaction = existing_transaction.first()

                transaction.block_hash = block
                transaction.block_number = block.number
                # transaction.cumulative_gas_used = ''
                transaction.created_contract_address_hash = None
                transaction.error = ''
                transaction.from_address_hash = self.get_address(
                    transaction_data['from']
                )
                transaction.gas = transaction_data['gas']
                transaction.gas_price = transaction_data['gasPrice']
                transaction.gas_used = (
                        transaction_data['gas'] * transaction_data['gasPrice']
                )
                transaction.hash = transaction_data['hash']
                transaction.index = transaction_data['transactionIndex']
                transaction.input = transaction_data['input']
                transaction.internal_transactions_indexed_at = None
                transaction.nonce = transaction_data['nonce']
                transaction.r = transaction_data['r']
                transaction.s = transaction_data['s']
                # transaction.status = ''
                transaction.to_address_hash = self.get_address(
                    transaction_data['to']
                )
                transaction.v = transaction_data['v']
                transaction.value = transaction_data['value']
                transaction.save()

            else:
                transaction = Transaction()

                transaction.block_hash = block
                transaction.block_number = block.number
                # transaction.cumulative_gas_used = ''
                transaction.created_contract_address_hash = None
                transaction.error = ''
                transaction.from_address_hash = self.get_address(
                    transaction_data['from']
                )
                transaction.gas = transaction_data['gas']
                transaction.gas_price = transaction_data['gasPrice']
                transaction.gas_used = (
                   transaction_data['gas'] * transaction_data['gasPrice']
                )
                transaction.hash = transaction_data['hash']
                transaction.index = transaction_data['transactionIndex']
                transaction.input = transaction_data['input']
                transaction.internal_transactions_indexed_at = None
                transaction.nonce = transaction_data['nonce']
                transaction.r = transaction_data['r']
                transaction.s = transaction_data['s']
                # transaction.status = ''
                transaction.to_address_hash = self.get_address(
                    transaction_data['to']
                )
                transaction.v = transaction_data['v']
                transaction.value = transaction_data['value']
                transaction.save()

        # Create uncle block if exists
        for uncle in block_data['uncles']:
            uncle_info = w3_client.eth.getBlock(uncle)

            uncle_data = web3_to_dict(uncle_info)

            miner = self.get_address(uncle_data['miner'])

            existing_uncle_block = Block.objects.filter(
                hash=uncle_data['hash']
            )

            if existing_uncle_block.exists():
                uncle_block = existing_uncle_block.first()
                uncle_block.consensus = False
                uncle_block.difficulty = uncle_data['difficulty']
                uncle_block.gas_limit = uncle_data['gasLimit']
                uncle_block.gas_used = uncle_data['gasUsed']
                uncle_block.hash = uncle_data['hash']
                uncle_block.miner = miner
                uncle_block.nonce = uncle_data['nonce']
                uncle_block.number = uncle_data['number']
                uncle_block.parent_hash = Block.objects.filter(
                    hash=uncle_data['parentHash']
                ).first()
                uncle_block.size = uncle_data['size']
                uncle_block.timestamp = uncle_data['timestamp']
                uncle_block.total_difficulty = uncle_data['totalDifficulty']
                uncle_block.save()
            else:
                uncle_block = Block()
                uncle_block.consensus = False
                uncle_block.difficulty = uncle_data['difficulty']
                uncle_block.gas_limit = uncle_data['gasLimit']
                uncle_block.gas_used = uncle_data['gasUsed']
                uncle_block.hash = uncle_data['hash']
                uncle_block.miner = miner
                uncle_block.nonce = uncle_data['nonce']
                uncle_block.number = uncle_data['number']
                uncle_block.parent_hash = Block.objects.filter(
                    hash=uncle_data['parentHash']
                ).first()
                uncle_block.size = uncle_data['size']
                uncle_block.timestamp = uncle_data['timestamp']
                uncle_block.total_difficulty = uncle_data['totalDifficulty']
                uncle_block.save()

            # Save relation between nephew and uncle
            SecondDegreeRelation.objects.get_or_create(
                nephew_hash=block,
                uncle_hash=uncle_block,
                defaults={
                    'uncle_fetched_at': block.timestamp
                }
            )

            # Save transaction relation for uncle block
            transaction_index = 0
            for transaction in uncle_data['transactions']:
                transaction = Transaction.objects.filter(hash=transaction)

                if not transaction.exists():
                    continue

                Fork.objects.create(
                    hash=transaction.first(),
                    index=transaction_index,
                    uncle_hash=uncle_block
                )

                transaction_index += 1

        return JsonResponse(status=200, data=block_data, safe=False)

    def get_address(self, address):
        """
        Retrieve or create a Address
        :param address: hash
        :return: Address instance
        """
        address, _ = Address.objects.get_or_create(
            hash=address
        )
        return address


class GetAddressInfoView(APIView):
    def get(self, request, *args, **kwargs):
        address_hash = kwargs['hash']

        try:
            address = Address.objects.get(
                hash=address_hash
            )
        except ObjectDoesNotExist:
            address_data = {}
            return JsonResponse(status=404, data=address_data)

        address_data = {
            'hash': address.hash
        }

        return JsonResponse(data=address_data)


class GetBlockInfoView(APIView):
    def get(self, request, *args, **kwargs):
        block_hash = kwargs['hash']

        try:
            block = Block.objects.get(hash=block_hash)
        except ObjectDoesNotExist:
            block_data = {}
            return JsonResponse(status=404, data=block_data)

        transactions = Transaction.objects.filter(
            block_hash=block
        )

        block_data = {
            'difficulty': block.difficulty,
            'gas_limit': block.gas_limit,
            'gas_used': block.gas_used,
            'hash': block.hash,
            'block_number': block.number,
            'parent_hash': block.parent_hash.hash,
            'size': block.size,
            'total_difficulty': block.total_difficulty,
            'transactions': [
                {
                    'hash': transaction.hash,
                    'index': transaction.index,
                    'from': transaction.from_address_hash.hash,
                    'to': transaction.to_address_hash.hash,
                    'transaction_url': reverse(
                        'explorer:get_transaction_info',
                        transaction.hash
                    ),
                    'from_url': reverse(
                        'explorer:get_address_info',
                        transaction.from_address_hash.hash
                    ),
                    'to_url': reverse(
                        'explorer:get_transaction_info',
                        transaction.to_address_hash.hash
                    )

                } for transaction in transactions
            ]
        }

        return JsonResponse(data=block_data)


class GetTransactionInfoView(APIView):
    def get(self, request, *args, **kwargs):
        transaction_hash = kwargs['hash']

        try:
            transaction = Transaction.objects.get(hash=transaction_hash)
        except ObjectDoesNotExist:
            transaction_data = {}
            return JsonResponse(status=404, data=transaction_data)

        transaction_data = {
            'block_hash': transaction.block_hash.hash,
            'block_number': transaction.block_number,
            'created_contract_address_hash':
                transaction.created_contract_address_hash.hash,
            'error': transaction.error,
            'from_address_hash': transaction.from_address_hash.hash,
            'gas': transaction.gas,
            'gas_price': transaction.gas_price,
            'gas_used': transaction.gas_used,
            'hash': transaction.hash,
            'index': transaction.index,
            'input': transaction.input,
            'internal_transactions_indexed_at':
                transaction.internal_transactions_indexed_at,
            'nonce': transaction.nonce,
            'r': transaction.r,
            's': transaction.s,
            'status': transaction.status,
            'to_address_hash': transaction.to_address_hash.hash,
            'v': transaction.v,
            'value': transaction.value,
            'block_url': reverse(
                'explorer:get_block_info',
                transaction.block_hash.hash
            ),
            'contract_address_hash': self.get_contract_address_url(
                transaction.created_contract_address_hash.hash
            ),
            'from_address_url': reverse(
                'explorer:get_address_info',
                transaction.from_address_hash.hash
            ),
            'to_address_url': reverse(
                'explorer:get_address_info',
                transaction.to_address_hash.hash
            )
        }

        return JsonResponse(transaction_data)

    def get_contract_address_url(self, address_hash):
        if not address_hash:
            return ''

        return reverse('explorer:get_address_info', address_hash)
