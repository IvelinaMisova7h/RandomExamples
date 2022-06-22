import math
n = int(input())

print('%' * (2 * n))
num_rows = n

if n % 2 == 0:
    num_rows -= 1

for i in range(0, num_rows):
    print('%', end='')

    if i == math.floor(num_rows / 2):
        print((' ' * (n - 2)) + '**' + (' ' * (n - 2)))
    else:
        print(' ' * (2 * n - 2))

    print('%', end='')

print('%' * (2 * n))
