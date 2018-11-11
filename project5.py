import io
student_names = io.open("student.txt", "r", encoding="utf-8")
result_txt = io.open("result.txt", "w", encoding="utf-8")

count = 0
marks_sum = 0
result_mark = 0
result_rating = 0

try:
    for student in student_names:
        marks = input("Введите через пробел текущие оценки ученика: {} ".format(student))
        marks = marks.split(" ")
        for mark in marks:
            count += 1
            mark = int(mark)
            marks_sum += mark
        result_rating = round((marks_sum / count), 2)
        result_mark = round(result_rating)
        result_txt.write("{} - рейтинг: {}, оценка: {} ".format(student, result_rating, result_mark))
        count = 0
        marks_sum = 0
except ValueError:
    print('Ошибка. Перезапустите программу и попробуйте снова.')

