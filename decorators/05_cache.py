# from functools import wraps
#
#
# def cache(func):
#     @wraps(func)
#     def wrapper(n):
#         num = func(n)
#         if n not in wrapper.log:
#             wrapper.log[n] = num
#         return wrapper.log[n]
#     wrapper.log = {}
#     return wrapper


# class cache:
#     def __init__(self, func):
#         self.func = func
#         self.log = {}
#
#     def __call__(self, n):
#         # if n not in self.log:
#         if n == 0:
#             self.log[n] = n
#         elif n == 1:
#             self.log[0] = 0
#             self.log[n] = n
#         else:
#             self.log[n] = self(n - 1) + self(n - 2)
#         return self.log[n]


def cache(func):
    def wrapper(n):
        wrapper.log[n] = func(n)
        if n == 1:
            wrapper.log[0] = 0
        return wrapper.log[n]
    wrapper.log = {}
    return wrapper



@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(1)
print(fibonacci.log)
fibonacci.log = {}

fibonacci(0)
print(fibonacci.log)
fibonacci.log = {}

fibonacci(4)
print(fibonacci.log)
