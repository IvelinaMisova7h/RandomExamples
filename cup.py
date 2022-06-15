n = int(input())

width = 5 * n
dots = n
hashtags = width - dots * 2

for i in range(1, n//2 + 1):
    print('.' * dots + '#' * hashtags + '.' * dots)
    dots = dots + 1
    hashtags = width - dots * 2

middle_dots = width - 2 - 2 * dots

for i in range(1, n//2+2):
    print('.' * dots + '#' + '.' * middle_dots + '#' + '.' * dots)
    dots += 1
    middle_dots -= 2
print('.' * (dots - 1) + '#' * (middle_dots + 4) + '.' * (dots - 1))

hashtags = n + 4
dots = (width - hashtags)//2
for i in range(1, n//2+1):
    print('.' * dots + '#' * hashtags + '.' * dots)

static_dots = (width - 10)//2

print('.' * static_dots + 'D^A^N^C^E^' + '.' * static_dots)

for i in range(1, n//2+2):
    print('.' * dots + '#' * hashtags + '.' * dots)