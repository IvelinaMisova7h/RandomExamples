import math

budget = float(input())
width = float(input())
length = float(input())
side_of_triangle = float(input())
height_of_triangle = float(input())
price_of_one_tile = float(input())
amount_for_master = float(input())

floor_area = width * length
tile_area = side_of_triangle * height_of_triangle/2
necessary_tiles = math.ceil(floor_area / tile_area) + 5
total_sum = necessary_tiles * price_of_one_tile + amount_for_master

left_money = budget - total_sum
need_money = total_sum - budget
if budget >= total_sum:
    print(f"{left_money:.2f} lv left.")
else:
    print(f"You'll need {need_money:.2f} lv more.")