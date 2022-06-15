x = float(input())
y = float(input())
h = float(input())

front_back_walls = x * x * 2 - 1.2 * 2
side_walls = x * y * 2 - 1.5 * 1.5 * 2
roof_side_parts = x * y * 2
roof_front_back = (x * h) / 2 * 2

red = (roof_front_back + roof_side_parts) / 4.3
green = (front_back_walls + side_walls) / 3.4
print(f'{green:.2f}')
print(f'{red:.2f}')
