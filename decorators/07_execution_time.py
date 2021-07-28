# from time import time
#
# class exec_time:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         start = time()
#         self.func(*args, **kwargs)
#         end = time()
#         return end - start

from timeit import default_timer


def exec_time(func):
    def wrapper(*args):
        start = default_timer()
        func(*args)
        end = default_timer()
        return end - start
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))
