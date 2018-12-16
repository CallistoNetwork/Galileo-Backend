from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework.views import APIView

from web3 import Web3, WebsocketProvider

from .utils import web3_to_dict

from address.models import Address
from blocks.models import Block
from transactions.models import Transaction


import json


class SaveView(View):

    def get(self, request, *args, **kwargs):
        parity_url = settings.PARITY_NODE_URL

        w3_client = Web3(WebsocketProvider(parity_url))

        block_info = w3_client.eth.getBlock('latest')

        block_data = web3_to_dict(block_info)

        # miner = self.get_address(block_data['miner'])
        #
        # block = Block()
        #
        # block.difficulty = block_data['difficulty']
        # block.gas_limit = block_data['gasLimit']
        # block.gas_used = block_data['gasUsed']
        # block.hash = block_data['hash']
        # block.miner = miner
        # block.nonce = block_data['nonce']
        # block.number = block_data['number']
        # block.parent_hash = Block.objects.filter(
        #     hash=block_data['parentHash']
        # ).first()
        # block.size = block_data['size']
        # block.timestamp = block_data['timestamp']
        # block.total_difficulty = block_data['totalDifficulty']
        # block.save()
        #
        # for transaction in block_data['transactions']:
        #     transaction_info = w3_client.eth.getTransaction(transaction)
        #     transaction_data = web3_to_dict(transaction_info)
        #
        #     transaction = Transaction()
        #
        #     transaction.block_hash = block.id
        #     transaction.block_number = block.number
        #     transaction.cumulative_gas_used = ''
        #     transaction.created_contract_address_hash = ''
        #     transaction.error = ''
        #     transaction.from_address_hash = self.get_address(
        #         transaction_data['from']
        #     )
        #     transaction.gas = transaction_data['gas']
        #     transaction.gas_price = transaction_data['gasPrice']
        #     transaction.gas_used = ''
        #     transaction.hash = transaction_data['hash']
        #     transaction.index = transaction_data['transactionIndex']
        #     transaction.input = transaction_data['input']
        #     transaction.internal_transactions_indexed_at = None
        #     transaction.nonce = transaction_data['nonce']
        #     transaction.r = transaction_data['r']
        #     transaction.s = transaction_data['s']
        #     transaction.status = ''
        #     transaction.to_address_hash = self.get_address(
        #         transaction_data['to']
        #     )
        #     transaction.v = transaction_data['v']
        #     transaction.value = transaction_data['value']
        #     transaction.save()
        #
        # for uncle in block_data['uncles']:
        #     uncle_info = w3_client.eth.getBlock(uncle)
        #
        #     uncle_data = web3_to_dict(uncle_info)
        #
        #     miner = self.get_address(uncle_data['miner'])
        #
        #     block = Block()
        #
        #     block.difficulty = uncle_data['difficulty']
        #     block.gas_limit = uncle_data['gasLimit']
        #     block.gas_used = uncle_data['gasUsed']
        #     block.hash = uncle_data['hash']
        #     block.miner = miner
        #     block.nonce = uncle_data['nonce']
        #     block.number = uncle_data['number']
        #     block.parent_hash = Block.objects.filter(
        #         hash=uncle_data['parentHash']
        #     )
        #     block.size = uncle_data['size']
        #     block.timestamp = uncle_data['timestamp']
        #     block.total_difficulty = uncle_data['totalDifficulty']
        #     block.save()

        return JsonResponse(status=200, data=self.get_block(), safe=False)

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
    pass


class GetBlockInfoView(APIView):
    def get(self, request, *args, **kwargs):
        print(kwargs['hash'])

        return JsonResponse({'hash': kwargs['hash']})


class GetTransactionInfoView(APIView):
    pass
