def tags(n):
    def decorator(func):
        def wrapper(*arg):
            return f"<{n}>{func(*arg)}</{n}>"
        return wrapper
    return decorator


@tags('a')
@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
