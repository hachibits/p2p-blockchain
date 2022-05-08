from Blockchain import Blockchain
import hashlib

blockchain = Blockchain()
t1 = blockchain.addTransaction("Satoshi|Mike|5 BTC")
t2 = blockchain.addTransaction("Mike|Satoshi|1 BTC")
t3 = blockchain.addTransaction("Satoshi|Hal Finney|5 BTC")
blockchain.newBlock(12345)
t1 = blockchain.addTransaction("Satoshi|Mike|5 BTC")
t2 = blockchain.addTransaction("Mike|Satoshi|1 BTC")
t3 = blockchain.addTransaction("Satoshi|Hal Finney|5 BTC")
blockchain.newBlock(6789)
blockchainList = blockchain.blockchain
blockchainLen = len(blockchainList)

class TestClass():
    '''Check calculateHash'''
    def test_one(self):
        global blockchain
        global blockchainList
        assert blockchain.calculateHash(blockchainList[0]) == "ce71ceece1a8e1bbae72275721f48a2aa1912f8b21e28602612a8d642002d75b"

    '''Test currentHash'''
    def test_two(self):
        global blockchain
        global blockchainList
        assert blockchainList[1]["currentHash"] == "4a684602ab084b0c029320f7c0009e5d096b608eb6752076aef6081e8f1ac14e"
        
    '''Test links between blocks'''
    def test_three(self):
        index = 0
        global blockchainList
        global blockchainLen
        while index != blockchainLen - 1:
            assert blockchainList[blockchainLen - index - 1]["previousHash"] == blockchain.calculateHash(blockchainList[blockchainLen - index - 2])
            index += 1

