class HashTable:
    """"The HashTable should have an attribute called array of type: list, where all the values will be stored.
        Upon initialization the default length of the array should be 4.
        After each addition of an element if the HashTable gets too populated,
        double the length of the array and re-add the existing data.
        You are not allowed to inherit any classes.
        Feel free to implement your own functionality (and unit tests) or to write the methods by yourself."""

    def __init__(self):
        self.array = [None, None, None, None]
        self.count = 1

    def hash(self, key: str):  # a function that should figure out where to store the key - value pair
        total = 0
        for i in range(len(key)):
            total += ord(key[i]) * (7**i)
        return (len(key) * total)

    def add(self, key: str, value: any):  # adds a new key - value pair usign the hash function
        if not self.count % len(self.array):
            self.array.extend([None for _ in range(len(self.array))])
        self.array[self.hash(key)] = {key: value}
        self.count += 1

    def get(self, key: str):  # returns the value corresponding to the given key
        return self.array[self.hash(key)][key]

    #  additional "magic" methods, that will make the code in the example work correctrly


h = HashTable()
h.add("weer", 1)
h.add("wer", 2)
h.add("er", 3)
print(h.array)
h.add("we", 4)
print(h.array)
h.add("wee", 5)
print(h.array)
h.add("seeer", 6)
h.add("ersa", 7)
h.add("wed", 8)
print(h.array)
h.add("wcee", 9)
print(h.array)
print(h.get("er"))
