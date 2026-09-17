class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.hashset = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        if key not in self.hashset[key % self.size]:
            self.hashset[key % self.size].append(key)

    def remove(self, key: int) -> None:
        if key in self.hashset[key % self.size]:
            self.hashset[key % self.size].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hashset[key % self.size]


if __name__ == "__main__":
    obj = MyHashSet()

    obj.add(1)
    obj.add(2)

    print(obj.contains(1))  # True
    print(obj.contains(3))  # False

    obj.add(2)
    print(obj.contains(2))  # True

    obj.remove(2)
    print(obj.contains(2))  # False

        
        



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)