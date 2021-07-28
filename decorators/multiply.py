def multiply(n):
    def decorator(ref_function):
        def wrapper(params):
            return n * ref_function(params)
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
