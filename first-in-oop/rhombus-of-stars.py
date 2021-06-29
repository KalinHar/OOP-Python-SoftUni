def print_row(n_spaces, n_stars):
    print(f'{" " * n_spaces}{"* " * n_stars}*')


n = int(input())
for i in range(n):
    print_row(n-i-1, i)
for i in range(1, n):
    print_row(i, n-i-1)
