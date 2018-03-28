import os
import asyncio
from functools import partial
from .connect import eth
from .views import format_block_info, format_token_transfers
from .tokens import generate_token_contracts


async def display_loop(filter_formatters, poll_interval=1):
    while True:
        for event_filter, formatter in filter_formatters.items():
            new_entries = event_filter.get_new_entries()
            if new_entries:
                print(formatter(new_entries))
        await asyncio.sleep(poll_interval)


def main():
    block_filter = eth.filter('latest')
    token_transfer_filters = {ticker: contract.eventFilter('Transfer')
                              for ticker, contract in generate_token_contracts()}
    filter_formatters = {
        block_filter: format_block_info,
        **{token_filter: partial(format_token_transfers, ticker)
           for ticker, token_filter in token_transfer_filters.items()}
    }
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.gather(
            display_loop(filter_formatters, 1)))
    finally:
        loop.close()


if __name__ == '__main__':
    main()
