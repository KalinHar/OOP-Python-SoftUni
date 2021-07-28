from time import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print(end - start)
        return res
    return wrapper


@measure_time
def counter(n):
    a = 0
    for i in range(n):
        a = i
    return a


print(counter(10000000))
