student_names = open("student.txt", "r")
result_txt = open("result.txt", "w")
count = 0
marks_sum = 0
result_mark = 0
result_rating = 0

for student in student_names:
    marks = input("Введите через пробел текущие оценки ученика: {} ".format(student))
    marks = marks.split(" ")
    for mark in marks:
        count += 1
        mark = int(mark)
        marks_sum += mark
    result_rating = round((marks_sum / count), 2)
    result_mark = round(result_rating)
    print("{} - rating: {}, mark: {} ".format(student, result_rating, result_mark), file=result_txt)
    count = 0
    marks_sum = 0

