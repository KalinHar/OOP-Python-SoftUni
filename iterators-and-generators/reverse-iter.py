class reverse_iter:  # iterator
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterable:
            return self.iterable.pop()
        else:
            raise StopIteration


def first_n(n):  # generator
    start_num = 1
    while start_num <= n:
        yield start_num
        start_num += 1


itersss = reverse_iter([1, 2, 3, 4, 5])

for num in itersss:
    print(f"sum to {num} is {sum(first_n(num))}")

# -------------------------------------------------


def genrange(start, stop):
    while start <= stop:
        yield start
        start += 1


print(list(genrange(1, 10)))
