class HashTable:
    def __init__(self):
        self.size = 100
        self.table = [None for i in range(self.size)]

    def get_hash(self,key):
        h = 0
        for letter in key:
            h += ord(letter)
        return h % self.size
    
    def insert(self,key,value):
        index = self.get_hash(key)
        if self.table[index] is None:
            self.table[index] = value
