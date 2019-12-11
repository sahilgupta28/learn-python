blockchain = [1]

def getLastElement():
    return blockchain[-1]


def addTransaction(amount, last_element=[1]):
    blockchain.append([last_element, amount])


addTransaction(1.4)
addTransaction(13.3, getLastElement())
addTransaction(45, getLastElem)
print(blockchain)