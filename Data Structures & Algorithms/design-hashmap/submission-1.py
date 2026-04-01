class MyHashMap:

    def __init__(self):

        self.hash_map = {}
        self.DELETED = object()
        

    def put(self, key: int, value: int) -> None:

        if key in self.hash_map:

            self.hash_map[key] = value
        self.hash_map[key] = value
        

    def get(self, key: int) -> int:

        if key in self.hash_map and self.hash_map[key] != self.DELETED:
            return self.hash_map[key]
        else:
            return -1
        

    def remove(self, key: int) -> None:

        if key in self.hash_map:
            self.hash_map[key] = self.DELETED
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)