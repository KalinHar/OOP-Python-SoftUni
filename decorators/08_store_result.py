class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self,*args):
        with open('result.txt', 'a+') as f:
            f.write(f"Function '{self.func.__name__}' was called. Result: {self.func(*args)}\n")


# def store_results(func):
#     def wrapper(*args):
#         return print(f"Function '{func.__name__}' was called. Result: {func(*args)}")
#     return wrapper


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
