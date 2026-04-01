class MyHashSet:

    def __init__(self):
        self.hash_ = [None for i in range(1000) ]
        

    def add(self, key: int) -> None:

        

        index = int(key % len(self.hash_))

        while self.hash_[index] is not None:
            
            if self.hash_[index] == key:
                return
            
            index = int((index + 1) % len(self.hash_))


        self.hash_[index] = key
            



        
        

    def remove(self, key: int) -> None:

        index = int(key % len(self.hash_))

        while self.hash_[index] is not None:

            if self.hash_[index] == key:
                self.hash_[index] = None
            
            index = int((index + 1) % len(self.hash_))

        
        

    def contains(self, key: int) -> bool:


        index = int(key % len(self.hash_))

        while self.hash_[index] is not None:
            if self.hash_[index] == key:
                return True

            index = int((index + 1) % len(self.hash_))
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)