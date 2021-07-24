def squares(n):
    # start_num = 1
    # while start_num <= n:
    #     yield start_num ** 2
    #     start_num += 1

    for i in range(1, n + 1):
        yield i ** 2


print(list(squares(5)))
print(sum(squares(3)))
