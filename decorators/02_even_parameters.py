def even_parameters(func):
    def wrapper(*params):
        even_nums = [el for el in params if isinstance(el, int) and el % 2 == 0]
        if len(even_nums) == len(params):
            return func(*params)
        return "Please use only even numbers!"
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
