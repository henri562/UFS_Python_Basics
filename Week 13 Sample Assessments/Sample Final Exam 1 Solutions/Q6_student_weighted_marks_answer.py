"""
Student marks
"""


def calculate_weighted_mark(student, weight):
    weighted_mark = 0
    for i in range(0, 4):
        weighted_mark += student[i + 1] * weight[i]
    return weighted_mark


def calculate_grade(mark):
    if mark >= 85:
        grade = 'A'
    elif mark >= 70:
        grade = 'B'
    elif mark >= 50:
        grade = 'C'
    elif mark >= 40:
        grade = 'D'
    else:
        grade = 'F'
    return grade


S9002 = ['Kevin-Hugh Hu', 76, 79, 76, 80]
S9014 = ['Serena Wills', 95, 98, 99, 100]
S9026 = ['Sarah Lee-Breu', 27, 21, 42, 52]
S9121 = ['Felicia Nickels', 7, 33, 58, 37]
S9165 = ['Andreas Liu', 46, 72, 67, 88]
S9199 = ['Christabel Park', 79, 79, 63, 44]
S9200 = ['Roger Roger', 42, 26, 7, 25]
S9217 = ['Matthew Rodi', 74, 96, 97, 94]

student = [S9002, S9014, S9026, S9121, S9165, S9199, S9200, S9217]

weight = [0.5, 0.15, 0.25, 0.1]

print(f"{'Student':<20}{'Mark':<12}{'Grade'}")
for i in student:
    w_mark = calculate_weighted_mark(i, weight)
    print(f"{i[0]:<20}{str(round(w_mark, 2)):<12}{calculate_grade(w_mark)}")
