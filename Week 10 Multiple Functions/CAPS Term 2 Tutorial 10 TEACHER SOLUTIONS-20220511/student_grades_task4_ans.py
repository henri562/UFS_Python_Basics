'''
A file to calculate student grades,
highest mark, average mark
and display this data effectively
'''
# student details
# The first element is the name of the student,
# the second is their English mark, the third is their maths mark
# and the fourth is their computing mark
John = ['John', 14, 45, 62]
Cynthia = ['Cynthia', 58, 78, 91]
Osman = ['Osman', 74, 81, 60]
Karen = ['Karen', 94, 94, 88]
Jason = ['Jason', 48, 56, 56]
students = [John, Cynthia, Osman, Karen, Jason]


# a function that returns the average mark
# takes student as a parameter
def av_mark(student):
    return (student[1] + student[2] + student[3]) / 3


def print_marks(student):
    statement = 'Student Name: ' + student[0] + '\n'
    statement += 'English Mark: ' + str(student[1]) + '\n'
    statement += 'Maths Mark: ' + str(student[2]) + '\n'
    statement += 'Computing Mark: ' + str(student[3])
    return statement


def calc_grade(student):
    average_mark = av_mark(student)
    if average_mark < 50:
        grade = 'Fail'
    elif average_mark < 70:
        grade = 'C'
    elif average_mark < 85:
        grade = 'B'
    else:
        grade = 'A'
    return grade


for s in students:
    print(print_marks(s))
    print('Average mark: %.1f' % av_mark(s))
    print('Grade: %s.' % calc_grade(s))
    print()
