import os
from functools import partial
import gevent
from .connect import eth
from .views import format_block_info, format_token_transfers
from .tokens import generate_token_contracts
from .utils import print_flush, cache_tx_total


def fetch_and_print(event_filter, formatter, poll_interval=1):
    while True:
        new_entries = event_filter.get_new_entries()
        if new_entries:
            print_flush(formatter(new_entries))
        gevent.sleep(poll_interval)


def main():
    block_filter = eth.filter('latest')
    token_transfer_filters = {ticker: contract.eventFilter('Transfer')
                              for ticker, contract in generate_token_contracts()}
    filter_formatters = {
        block_filter: format_block_info,
        **{token_filter: partial(format_token_transfers, ticker)
           for ticker, token_filter in token_transfer_filters.items()}
    }

    try:
        pollers = [gevent.spawn(fetch_and_print, event_filter, formatter)
                   for event_filter, formatter in filter_formatters.items()]
        print('Starting event filter pollers')
        gevent.joinall(pollers)
    finally:
        gevent.killall(pollers)
        from .calculate_stats import last_summed_tx_block, last_summed_tx_total
        cache_tx_total(last_summed_tx_block, last_summed_tx_total)


if __name__ == '__main__':
    main()
