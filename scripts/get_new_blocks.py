import asyncio
from web3 import Web3, WebsocketProvider

PARITY_NODE_URL = 'ws://192.168.10.2:8546'

w3 = Web3(WebsocketProvider(PARITY_NODE_URL))


def send_to_endpoint(block_hash):
    print(block_hash.hex())


async def get_blocks(w3_filter, poll_intervall):
    while w3.isConnected():
        for event in w3_filter.get_new_entries():
            send_to_endpoint(event)
        await asyncio.sleep(poll_intervall)


def main():
    w3_filter = w3.eth.filter('latest')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                get_blocks(w3_filter, 2)
            )
        )
    finally:
        loop.close()


if __name__ == '__main__':
    main()
