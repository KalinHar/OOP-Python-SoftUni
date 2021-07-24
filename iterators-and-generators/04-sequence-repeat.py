class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.start = number + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == 1:
            raise StopIteration
        self.start -= 1
        if self.number - self.start >= len(self.sequence):
            ind = (self.number - self.start) % len(self.sequence)
        else:
            ind = self.number - self.start
        return self.sequence[ind]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
