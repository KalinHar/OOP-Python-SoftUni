class HashTable:
    """"The HashTable should have an attribute called array of type: list, where all the values will be stored.
        Upon initialization the default length of the array should be 4.
        After each addition of an element if the HashTable gets too populated,
        double the length of the array and re-add the existing data.
        You are not allowed to inherit any classes.
        Feel free to implement your own functionality (and unit tests) or to write the methods by yourself."""

    def __init__(self):
        self.array = [None] * 2

    def extend_array(self):
        new_array = [None for _ in range(len(self.array) * 2)]
        for kvp in self.items():
            k, v = kvp
            new_array[self.hash(k)] = (k, v)
        self.array = new_array

    def hash(self, key: str):  # a function that should figure out where to store the key - value pair
        total = 0
        for i in range(len(key)):
            total += ord(key[i]) * (7**i)
        return total % len(self.array)

    def add(self, key: str, value: any):  # adds a new key - value pair using the hash function
        if self.array[self.hash(key)] != None:  # check for collision and extend array if it
            self.extend_array()
            self.add(key, value)
        self.array[self.hash(key)] = (key, value)

    def get_value(self, key: str):  # returns the value corresponding to the given key
        return self.array[self.hash(key)][1]

    def get_pair(self, key: str):  # returns the kvp corresponding to the given key
        return self.array[self.hash(key)]

    def items(self):
        return [kvp for kvp in self.array if kvp]

    #  additional "magic" methods, that will make the code in the example work correctrly


h = HashTable()
h.add("weer", 1)
h.add("wer", 2)
h.add("er", 3)
h.add("we", 4)
h.add("wee", 5)
h.add("seeer", 6)
h.add("ersa", 7)
h.add("wed", 8)
h.add("wcee", 9)
print(h.items())  # we have -> 9 elements => len array must be 8+1 = 16
print(len(h.array))  # but len = 32=2**5 => 1 unexpected collision was happened and 4 expected
print(h.get_value("er"))
print(h.get_pair("wcee"))
