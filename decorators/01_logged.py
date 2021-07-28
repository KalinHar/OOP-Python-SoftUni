def logged(func_ref):
    def wrapper(*params):
        res = func_ref(*params)
        return f"you called {func_ref.__name__}{params}\nit returned {res}"
    return wrapper


@logged
def func(*args):
    return 3 + len(args)

print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b

print(sum_func(1, 4))
