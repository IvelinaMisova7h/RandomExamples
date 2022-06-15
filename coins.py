n = float(input())

n = n * 100
count = 0
while n > 0:
    if n >= 200:
        n -= 200
        count += 1
    elif n >= 100:
        n -= 100
        count += 1
    elif n >= 50:
        n -= 50
        count += 1
    elif n >= 20:
        n -= 20
        count += 1
    elif n >= 10:
        n -= 10
        count += 1
    elif n >= 5:
        n -= 5
        count += 1
    elif n >= 2:
        n -= 2
        count += 1
    elif n >= 1:
        n -= 1
        count += 1
print(count)