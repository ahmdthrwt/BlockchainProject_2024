from hashlib import sha256


def updatehash(*args):
    """
    Function to update the hash of a block
    """
    hashing_text = ""
    h = sha256() 
    for arg in args:
        hashing_text += str(arg)

    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()


class Block:
    """
    Class to represent a block in the blockchain
    """
    data = None
    hash = None
    nonce = 0
    previous_hash = "0" * 64

    def __init__(self, data, number=0):
        self.data = data
        self.number = number

    def hash(self):
        return updatehash(self.previous_hash, self.number, self.data, self.nonce)

    def __str__(self):
        return "Block#: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s\n" % (
            self.number, self.hash(), self.previous_hash, self.data, self.nonce)


class Blockchain:
    """
    Class to represent the blockchain
    """
    difficulty = 4   # difficulty is the number of leading zeros required in the hash of the block 

    def __init__(self, chain=[]):
        self.chain = chain

    def add(self, block):
        self.chain.append(block)
    
    def remove(self, block):
        self.chain.remove(block) # in case we want to remove a block, we can do so by calling this method

    def mine(self, block):
        try: block.previous_hash = self.chain[-1].hash()
            # Set the previous hash of the block to the hash of the last block in the chain
            
        
        except IndexError: pass 
            # If the chain is empty, set the previous hash of the block to 0
            

        while True:
            # Increment the nonce of the block until the hash of the block has the required number of leading zeros
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block)
                break
            else:
                block.nonce += 1

def isValidChain(self):
    """
    This method checks if the blockchain is valid. It iterates over each block in the chain and checks two conditions:
    1. The previous hash of the current block should be equal to the hash of the previous block.
    2. The hash of the previous block should have the required number of leading zeros (as defined by the difficulty).
    If any of these conditions fail, the method returns False, indicating an invalid chain. If all blocks pass these conditions, it returns True.
    """
    for i in range(1, len(self.chain)):
        _previous = self.chain[i].previous_hash
        _current = self.chain[i-1].hash()

        if _previous != _current or _current[:self.difficulty] != "0"*self.difficulty:
            return False
    return True
  

def main():
    """
    This is the main function where the blockchain is initialized and some data is added to it.
    """
    blockchain = Blockchain()
    database = ["Hello World", "What's up", "Hello", "World"]
    
    """
        # Test 
    num = 0
    for data in database:
        num += 1
        Blockchain().mine(Block(data, num))

    for block in blockchain.chain:
        print(block)
    
    
        # Test to check if the blockchain is valid after modifying the data of a block
    blockchain.chain[2].data = "NEW DATA" 
    print(isValidChain(blockchain)) # False
    """


if __name__ == "__main__":
    main()