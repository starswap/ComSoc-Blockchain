import time
import hashlib
class Blockchain():
  def __init__(self,genesisBlock,difficulty):
    self.chain = []
    self.difficulty = difficulty    
    self.mineBlock(genesisBlock) 
  def mineBlock(self,block):
    block.work(self.difficulty)
    self.chain.append(block)
    print("Block Added with contents: " + block.textContent)
    print("Block hash is " + block.getHash())
  def validate(self):
    for i,item in enumerate(self.chain):
      if item.validate(self.difficulty) == False:
        return False
      if i != 0:
        if item.getHash() != self.chain[i-1].getHash():
          return False
      
    return True

class Block():
  def __init__(self,textContent,hashOfPreviousBlock="0"*32,timestamp=time.time(),nonce=0):
    self.textContent = textContent
    self.hashOfPreviousBlock = hashOfPreviousBlock
    self.nonce = nonce
    self.timestamp = timestamp    
    self.hash = self.getHash()
  def makeContent(self):
    self.content = str(self.textContent + str(self.timestamp) + self.hashOfPreviousBlock + str(self.nonce)).encode('utf-8')
    #print(self.content)
  def getHash(self):
    self.makeContent()
    self.hash = str(hashlib.sha256(self.content).hexdigest()) 
    return self.hash
  def work(self,difficulty):
    self.nonce = 0
    while not(self.getHash()[:difficulty] == "0"*difficulty):
      #print(self.hash)
      self.nonce += 1
    return True
  def validate(self,difficulty):
    return self.getHash()[:difficulty] == "0"*difficulty

start = time.time()
JamesCoin = Blockchain(Block("James is the genesis"),3)
JamesCoin.mineBlock(Block("Santosh is the most intriguing geographer"))
end = time.time()
print("Total time in seconds : " + str(end-start))