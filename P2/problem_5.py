import hashlib
from datetime import datetime

class Block:
    
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.previous = None
      self.index = 0


    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def get_hash(self):
        return self.hash

    def get_index(self):
        return self.index

class LinkedList:
    def __init__(self):
        self.tail = None

    def append(self, data):
        """ Append a value to the end of the list. """   
        now = datetime.now() 
        timestamp = now.strftime("%D %H:%M:%S")
        if self.tail is None:
            self.tail = Block(timestamp, data, '')
            return
        new_block = Block(timestamp, data, self.tail.get_hash())
        new_block.index = self.tail.get_index() + 1
        new_block.previous = self.tail
        self.tail = new_block

    def __repr__(self):
        block = self.tail
        while block:
            print("Block Start ============================")
            print("Index: {}".format(block.get_index()))
            print("Timestamp: " + block.timestamp)
            print("Data: " + block.data)
            print("SHA256 Hash: " + block.get_hash())
            print("Prev Hash: " + block.previous_hash)
            print("Block End====================================")
            block = block.previous
    pass

    def __str__(self):
        return_str = ""
        block = self.tail
        while block:
            return_str += "\nBlock Start ============================"
            return_str += "\nIndex: {}".format(block.get_index())
            return_str += "\nTimestamp: " + block.timestamp
            return_str += "\nData: " + block.data
            return_str += "\nSHA256 Hash: " + block.get_hash()
            return_str += "\nPrev Hash: " + block.previous_hash
            return_str += "\nBlock End===================================="
            block = block.previous
        return return_str

block_chain = LinkedList()

block_chain.append("Ahmed")
block_chain.append("Mohamed")
block_chain.append("Shendy")

print(block_chain)

block_chain = LinkedList()


print(block_chain)