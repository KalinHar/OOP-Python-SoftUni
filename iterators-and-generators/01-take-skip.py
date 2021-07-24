class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.multiply = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.multiply:
            raise StopIteration
        result = self.step * self.multiply
        self.multiply += 1
        return result


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
numbers = take_skip(10, 5)
for number in numbers:
    print(number)
