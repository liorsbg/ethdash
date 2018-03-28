from web3 import Web3, IPCProvider
import time

provider = IPCProvider('/root/geth1/.ethereum/geth.ipc')
web3 = Web3(provider)
eth = web3.eth


def getSyncProgress():
    sync_info = eth.syncing
    return 100.0 * sync_info.currentBlock / sync_info.highestBlock


eos_address = '0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0'
eos_contract = eth.contract(address=eos_address, abi=ecr20_abi)

def write_flush(o):
    sys.stdout.write(f'New Something: {o}')
    sys.stdout.flush()



from datetime import datetime as dt
dt.fromtimestamp(eth.getBlock('latest').timestamp)

eth.getTransaction('latest')

erc20_abi = json.load(open('/root/parity/ECR20ABI.json')) 
eos_address = '0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0'
eos_contract = eth.contract(address=eos_address, abi=ecr20_abi)
def get_EOS_transfers(block): 
    print(eos_contract.pastEvents("Transfer").get())

latest_filter = eth.filter('latest')
latest_filter.watch(get_EOS_transfers)
latest_filter.stop_watching()
