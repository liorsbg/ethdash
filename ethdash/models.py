

class Blocks:
    '''
    Convenience wrapper around eth.getBlock
    Allows treating the eth blockchain as a virtual list e.g.:
    >> blocks[0]    # First block
    >> blocks[-1]   # Latest block
    >> blocks[-3:]  # Last 3 blocks
    >> for b in blocks[-100:]: # lazily iterate over the last 100 blocks
    >>     # do cool stuff
    '''
    def __init__(self, eth):
        self._eth = eth
        self.get = eth.getBlock

    def __getitem__(self, val):
        if isinstance(val, int):
            return self._eth.getBlock(self._index_to_positive(val))
        else:
            # val is a slice object, indices converts to range tuple
            return (self._eth.getBlock(i) for i in range(*val.indices(len(self))))
    
    def __len__(self):
        # On geth, blockNumber will be 0 while syncing
        return (self._eth.blockNumber or self._eth.syncing.currentBlock) + 1

    def _index_to_positive(self, number):
        # Allow negative indexing
        return number if number >= 0 else len(self) + number
    
