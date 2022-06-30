k = int(input())
l = int(input())
m = int(input())
n = int(input())

for num_1 in range(k, 8+1):
    for num_2 in range(9, l-1, - 1):
        for num_3 in range(m, 8+1):
            for num_4 in range(9, n-1, -1):
                if (num_1 % 2 == 0 and not num_2 % 2 == 0) and (num_3 % 2 == 0 and not num_4 % 2 == 0):
                    if not num_1 == num_3 or not num_2 == num_4:
                        print(f"{num_1} {num_2} - {num_3} {num_4}")
                    else:
                        print('Cannot change the same player.')

