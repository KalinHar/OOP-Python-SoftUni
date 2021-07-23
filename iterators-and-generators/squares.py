def squares(n):
    start_num = 1
    while start_num <= n:
        yield start_num ** 2
        start_num += 1

print(list(squares(5)))