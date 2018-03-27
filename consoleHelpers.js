function syncStats() { 
    var s = eth.syncing
    return { 
        pendingStates: s.knownStates - s.pulledStates, 
        prcntStates: 100* s.pulledStates / s.knownStates, 
        remainingBlocks: s.highestBlock - s.currentBlock, 
        prcntBlocks: 100 * s.currentBlock / s.highestBlock }; 
    }
}

var tx0 = eth.getBlock(eth.syncing.currentBlock).transactions[0]