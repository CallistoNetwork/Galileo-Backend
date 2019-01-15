import asyncio
import requests
from django.urls import reverse
from web3 import Web3, WebsocketProvider
from parity.utils import web3_to_dict

PARITY_NODE_URL = 'ws://192.168.10.2:8546'

w3 = Web3(WebsocketProvider(PARITY_NODE_URL))


def send_to_endpoint(block_hash, w3_type):

    url = reverse('explorer:save', args=(block_hash.hex(), ))
    res = requests.get(f'http://clo.devgalileo.com:8000{url}')
    print(res.json().get('number'))



async def get_blocks(w3_filter, w3_type, poll_intervall):
    while w3.isConnected():
        for event in w3_filter.get_new_entries():
            send_to_endpoint(event, w3_type)
        await asyncio.sleep(poll_intervall)


def get_latest_block():
    w3_latest = w3.eth.filter('latest')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                get_blocks(w3_latest, 'latest', 2)
            )
        )
    finally:
        loop.close()


def run():
    get_latest_block()
