
from datetime import datetime
from .connect import eth
from .calculate_stats import sum_transactions, min_gas_price_for_block

def format_block_info(block_hashes):
    if not block_hashes:
        return ''
    
    # We only care about the most recent block    
    block_hash = block_hashes[-1]
    block = eth.getBlock(block_hash)
    return f'''New Block: {block_hash.hex()}
    Number of blocks: {block.number}
    Last block confirmation time: {datetime.fromtimestamp(block.timestamp).isoformat()}
    Total transactions: {sum_transactions()}
    Minimum gas price for last block (Gwei): {min_gas_price_for_block(block)/10**9}
    '''


def _format_token_transfer_info(event):
    if not event:
        return ''
    return f'{event.args._value/10**18}\t{event.args._from} ===> {event.args._to}\t{event.transactionHash.hex()}'

def format_token_transfers(ticker, events):
    if not events:
        return ''
    all_transfers = "\n".join(f'    {_format_token_transfer_info(event)}' for event in events)
    return f'{ticker}:\n{all_transfers}ֿ\n'