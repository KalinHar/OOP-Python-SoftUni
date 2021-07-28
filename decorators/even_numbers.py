def even_numbers(ref_func):
    def wrapper(nums):
        res = [n for n in nums if n % 2 == 0]
        return ref_func(res)
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
