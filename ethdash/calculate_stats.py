import logging
from .connect import eth
from .models import Blocks
from .utils import save_local_json, load_local_json, load_tx_total_cache

blocks = Blocks(eth)

last_summed_tx_block, last_summed_tx_total = load_tx_total_cache()


def sum_transactions():
    global last_summed_tx_block, last_summed_tx_total
    for b in blocks[last_summed_tx_block + 1:]:
        last_summed_tx_block, last_summed_tx_total = b.number, last_summed_tx_total + \
            eth.getBlockTransactionCount(b.hash)
        if not b.number % 1000:
            logging.debug(
                f'Counting txs: block: {last_summed_tx_block}, total: {last_summed_tx_total}')
    return last_summed_tx_total


def min_gas_price_for_block(block):
    if block.transactions:
        # eth.getTransaction sometimes returns None
        valid_transactions = filter(
            None, map(eth.getTransaction, block.transactions))
        return min(tx.gasPrice for tx in valid_transactions)
    else:
        # TODO: what would be the min price to get in if there were no transactions?
        return 0
