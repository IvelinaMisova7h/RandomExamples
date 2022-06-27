first_speed = int(input())
first_time = int(input())
second_time = int(input())
third_time = int(input())

minutes_per_hour = 60

first_interval_hours = first_time / minutes_per_hour
first_distance = first_speed * first_time

speed_up = first_speed + ((first_speed * 10) / 100)
second_interval_hours = second_time / minutes_per_hour
second_distance = speed_up * second_interval_hours


third_interval_hours = third_time / minutes_per_hour
third_distance = (speed_up - (speed_up * 0.05)) * third_interval_hours

total_km = first_distance + second_distance + third_distance
final_result = ("{:.2f}".format(total_km))
print("Total kilometers: ", final_result)
