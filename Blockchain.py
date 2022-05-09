import hashlib
import json
from time import time
import datetime

class Blockchain():
    def  __init__(self):
        self.blockchain = []
        self.pool = []
        self.poolLimit = 3
        self.newBlock(previousHash="9F86D081884C7D659A2FEAA0C55AD015A3BF4F1B2B0B822CD15D6C15B0F00A08", proof=100)

    def newBlock(self, proof, previousHash=None):
        block = {
            'index': len(self.blockchain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'transaction': self.pool,
            'proof': proof,
            'previousHash': previousHash or self.calculateHash(self.blockchain[-1]),
            'currentHash': self.currentHash(self.pool)
        }
        self.pool = []
        self.blockchain.append(block)

    def lastBlock(self):
        return self.blockchain[-1]

    def calculateHash(self, block):
        blockObject = json.dumps(block, sort_keys=True)
        blockString = blockObject.encode()
        rawHash = hashlib.sha256(blockString)
        hexHash = rawHash.hexdigest()
        return hexHash

    def addTransaction(self, transaction):
        if len(self.pool) < self.poolLimit:
            self.pool.append(transaction)
        lastBlock = self.lastBlock()
        return lastBlock['index'] + 1

    def currentHash(self, pool):
        currentTransactions = ""
        if len(pool) > 0:
            previousHash = self.calculateHash(self.lastBlock())
            currentTransactions += previousHash
            for transaction in pool:
                currentTransactions += transaction
            return hashlib.sha256(currentTransactions.encode()).hexdigest()

blockchain = Blockchain()
tx1 = blockchain.addTransaction("Satoshi|Mike|5 BTC")
tx2 = blockchain.addTransaction("Mike|Satoshi|1 BTC")
tx3 = blockchain.addTransaction("Satoshi|Hal Finney|5 BTC")
blockchain.newBlock(42)
print("Genesis block: ", blockchain.blockchain)
