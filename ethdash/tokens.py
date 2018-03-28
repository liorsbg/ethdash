import os
import json
from .connect import eth
from .utils import load_local_json

token_contract_addresses = load_local_json('token_config.json')
erc20_abi = load_local_json('ECR20ABI.json')

def generate_token_contracts():
    for ticker, address in token_contract_addresses.items():
        yield ticker, eth.contract(address=address, abi=erc20_abi)
