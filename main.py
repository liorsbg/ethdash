import os
import time
import logging
import json
from datetime import datetime
from pprint import pprint
from web3 import Web3, IPCProvider
# from models import Blocks

# logging.basicConfig(level=logging.DEBUG)

IPC_PATH = os.getenv('IPC_PATH', '/root/parity/.local/share/io.parity.ethereum/jsonrpc.ipc') # '/root/geth1/.ethereum/geth.ipc')

provider = IPCProvider(IPC_PATH)
web3 = Web3(provider)
eth = web3.eth

blocks = Blocks(eth)

erc20_abi = json.load(open('/root/parity/ECR20ABI.json')) 
eos_address = '0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0'
eos_contract = eth.contract(address=eos_address, abi=erc20_abi)

def get_EOS_transfers(block): 
    return eos_contract.pastEvents("Transfer").get()

# calculated ahead of time to save time.
last_summed_tx_block = 5328751
last_summed_tx_total = 190745916
# TODO: If not up to date, run this in background and return 'calculating...'
def sum_transactions():
    global last_summed_tx_block, last_summed_tx_total
    for b in blocks[last_summed_tx_block + 1:]:
        last_summed_tx_block, last_summed_tx_total = b.number, last_summed_tx_total + len(b.transactions)
        if not b.number % 1000:
            logging.debug(f'Counting txs: block: {last_summed_tx_block}, total: {last_summed_tx_total}')
    return last_summed_tx_total

def min_gas_price_for_block(block):
    if block.transactions:
        return min(eth.getTransaction(t).gasPrice for t in block.transactions)
    else:
        # TODO: review this assumption
        return 0


def display_block_info(block_hash):
    print(f'New Block: {block_hash}')
    block = eth.getBlock(block_hash)
    pprint({
        'number of blocks': block.number,
        'last block confirmation time': datetime.fromtimestamp(block.timestamp).isoformat(),
        'total transactions': sum_transactions(),
        'minimum gas price for last block': min_gas_price_for_block(block),
        'eos_transfers': get_EOS_transfers(block)
    })

latest_block_filter = eth.filter('latest')
latest_block_filter.watch(display_block_info)