def add_students():
    # a function to create a list of students
    # with GID, zNumber and computer mark

    st = []
    for i in range(1, 10):
        st.append(i)

    st[0] = ['G04O976', 'z6313834', 57]
    st[1] = ['G0432a1', 'z0261481', 97]
    st[2] = ['GO49620', 'z611168', 94]
    st[3] = ['G045824', 'z6247809', 99]
    st[4] = ['g045469', 'z638155507', 54]
    st[5] = ['G04130', 'Z6232395', 28]
    st[6] = ['G047353', 'z6360ab9', 38]
    st[7] = ['G0491191', 'x0183659', 98]
    st[8] = ['G044761', 'z6125160', 62]

    return st


def check_GID(student_GID):
    if len(student_GID) != 7:
        return 'Wrong length'
    if student_GID[0] != 'G':
        return 'Does not start with G'
    if student_GID[1] != '0':
        return 'Second character is not 0'
    for i in range(2, 7):
        try:
            temp = int(student_GID[i]) + 1
        except:
            return 'Not numeric'
    return True


def check_z_number(z_number):
    if len(z_number) != 8:
        return 'Wrong length'
    if z_number[0] != 'z':
        return 'Does not start with a z'
    if z_number[1] == '0':
        return 'Second character is a zero'
    for i in range(2, 8):
        try:
            temp = int(z_number[i]) + 1
        except:
            return 'not numeric'
    return True


def sort_by_comp_mark(student_list):
    # perform a selection sort on student list
    for i in range(0, len(student_list) - 1):
        for j in range(i + 1, len(student_list)):
            if student_list[i][2] < student_list[j][2]:
                temp = student_list[i]
                student_list[i] = student_list[j]
                student_list[j] = temp
    return student_list


# find students who scored at least mark
def find_top_students(student_list, mark):
    top_students = []
    for student in student_list:
        if student[2] >= mark:
            top_students.append(student)
    top_students = sort_by_comp_mark(top_students)
    return top_students


'''
Note this is a bubble sort, an alternative method of sorting
It is provided for students who are interested
'''


def bubble_sort_students(student_list):
    # go through the list and swap contiguous elements if necessary
    # go through the list until there is no swap
    swap_made = True
    while swap_made == True:
        swap_made = False
        for i in range(0, len(student_list) - 1):
            if student_list[i][2] < student_list[i + 1][2]:
                temp = student_list[i]
                student_list[i] = student_list[i + 1]
                student_list[i + 1] = temp
                swap_made = True
    return student_list


student_list = add_students()

for student in student_list:
    print(student[0], end='')
    if check_GID(student[0]) == True:
        print()
    else:
        print('. %s' % check_GID(student[0]))

# check each student's z-number and show errors as necesary
print()
for student in student_list:
    print(student[1], end='')
    if check_z_number(student[1]) == True:
        print()
    else:
        print(' \t%s' % check_z_number(student[1]))

student_list = sort_by_comp_mark(student_list)
for student in student_list:
    print(student)

# print off a list of students who scored 80 or more
print()
good_mark = 80
print('Top students who scored at least %d.' % good_mark)
top_student_list = find_top_students(student_list, 80)
print('GID         z-number         mark')
tab = [12, 29]
for student in top_student_list:
    print_line = ''
    for i in range(2):
        print_line += student[i]
        while len(print_line) < tab[i]:
            print_line += ' '
    print_line += str(student[2])
    print(print_line)
