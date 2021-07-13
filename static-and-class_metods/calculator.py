from functools import reduce


class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda a, b: a*b, args)

    @staticmethod
    def divide(*args):
        if not any(args[1:]):
            raise ValueError("Cannot divide by Zero!")
        return reduce(lambda a, b: a/b, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda a, b: a-b, args)


print(Calculator.divide(20, 2, 2))
print(Calculator.divide(0, 2, 2))
print(Calculator.multiply(20, 2, 2))
print(Calculator.subtract(20, 2, 2))
print(Calculator.add(20, 2, 2))
print()
print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
print(Calculator.divide(20, 0, 2))