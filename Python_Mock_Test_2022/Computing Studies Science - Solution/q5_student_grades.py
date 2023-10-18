"""
Student marks
"""


# should return the course mark for the student
def calculate_course_mark(student):
    course_mark = student[1] * 0.4 + student[2] * 0.6
    return course_mark


# should return a string representing the grade of the given marks
def calculate_grade(course_mark, class_mark, exam_mark):
    if (exam_mark < 40 or class_mark < 50) and course_mark >= 50:
        grade = 'UF'
    elif course_mark >= 50:
        grade = 'PS'
    else:
        grade = 'FL'
    return grade


S9002 = ['Kevin-Hugh Hu', 65, 40]
S9014 = ['Serena Wills', 95, 100]
S9026 = ['Sarah Lee-Breu', 45, 52]
S9121 = ['Felicia Nickels', 7, 37]
S9165 = ['Andreas Liu', 49, 88]
S9199 = ['Christabel Park', 79, 39]
S9200 = ['Roger Roger', 42, 25]
S9217 = ['Matthew Rodi', 74, 94]

student = [S9002, S9014, S9026, S9121, S9165, S9199, S9200, S9217]

l = 18
a = 10
print('Student Name'.ljust(l) + 'Mark'.ljust(l - a) + 'Grade')
for s in student:
    c_mark = calculate_course_mark(s)
    print(s[0].ljust(l) + str('%.2f' % c_mark).ljust(l - a) + calculate_grade(c_mark, s[1], s[2]))
