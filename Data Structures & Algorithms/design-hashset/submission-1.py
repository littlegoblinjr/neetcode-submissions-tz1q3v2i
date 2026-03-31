class MyHashSet:

    def __init__(self):
        self.MAX = 100000
        self.arr = [None for i in range(self.MAX)]
        

    def add(self, key: int) -> None:
        self.index_value = key % self.MAX
        self.arr[self.index_value] = key


        

    def remove(self, key: int) -> None:

        self.index_value = key % self.MAX

        self.arr[self.index_value] = None
        

    def contains(self, key: int) -> bool:

        self.index_value = key % self.MAX

        if self.arr[self.index_value]:
            return True
        else:
            return False
        


        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)