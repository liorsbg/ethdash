import sys
import os
import json

_TX_TOTAL_CACHE_NAME = 'tx_total_cache.json'
HARDCODED_TX_TOTAL_CACHE = {'last_summed_tx_block': 5337573,
                            'last_summed_tx_total': 191637969}


def current_directory():
    '''
    :return: Absolute path of file from which this function is run
    '''
    return os.path.dirname(os.path.realpath(__file__))


def load_local_json(name):
    try:
        return json.load(open(os.path.join(current_directory(), name)))
    except:
        return None


def save_local_json(name, data):
    try:
        json.dump(data, open(os.path.join(current_directory(), name), 'w'))
    except:
        pass


def load_tx_total_cache():

    cache = load_local_json(_TX_TOTAL_CACHE_NAME) or HARDCODED_TX_TOTAL_CACHE
    return cache['last_summed_tx_block'], cache['last_summed_tx_total']


def cache_tx_total(last_summed_tx_block, last_summed_tx_total):
    save_local_json(_TX_TOTAL_CACHE_NAME, {'last_summed_tx_block': last_summed_tx_block,
                                           'last_summed_tx_total': last_summed_tx_total})


def print_flush(s):
    sys.stdout.write(f'{s}\n')
    sys.stdout.flush()
