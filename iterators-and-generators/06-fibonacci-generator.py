def fibonacci():
    num, next_num = 0, 1
    while True:
        yield num
        num, next_num = next_num, num + next_num


generator = fibonacci()
for i in range(6):
    print(next(generator))
