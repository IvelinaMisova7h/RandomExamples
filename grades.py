count_students = int(input())

number_of_failed_students = 0
number_of_average_students = 0
number_of_good_students = 0
number_of_excellent_students = 0
total_result = 0

for i in range(count_students):
    grades_of_exam = float(input())
    total_result += grades_of_exam
    if grades_of_exam < 3:
        number_of_failed_students += 1
    elif 3 <= grades_of_exam <= 3.99:
        number_of_average_students += 1
    elif 4 <= grades_of_exam <= 4.99:
        number_of_good_students += 1
    elif 5 <= grades_of_exam <= 6:
        number_of_excellent_students += 1

percent_of_failed_students = (number_of_failed_students * 100) / count_students
percent_of_average_students = (number_of_average_students * 100) / count_students
percent_of_good_students = (number_of_good_students * 100) / count_students
percent_of_excellent_students = (number_of_excellent_students * 100) / count_students

average_sum = total_result / count_students


print(f"Top students: {percent_of_excellent_students:.2f}%")
print(f"Between 4.00 and 4.99: {percent_of_good_students:.2f}%")
print(f"Between 3.00 and 3.99: {percent_of_average_students:.2f}%")
print(f"Fail: {percent_of_failed_students:.2f}%")
print(f"Average: {average_sum:.2f}")




