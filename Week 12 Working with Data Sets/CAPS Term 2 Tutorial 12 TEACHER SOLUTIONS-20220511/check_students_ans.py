student_list = [
    ['G04O976', 'z6313834', 57],
    ['G0432a1', 'z0261481', 97],
    ['GO49620', 'z611168', 94],
    ['G045824', 'z6247809', 99],
    ['g045469', 'z638155507', 54],
    ['G04130', 'Z6232395', 28],
    ['G047353', 'z6360ab9', 38],
    ['G0491191', 'x0183659', 98],
    ['G044761', 'z6125160', 62],
]


# check that the student GID is correct
# 7 characters, starts with G, followed by 0, then 5 numbers
def check_GID(student_GID):
    if len(student_GID) != 7:
        return 'Wrong length'
    if student_GID[0] != 'G':
        return 'Does not start with G'
    if student_GID[1] != '0':
        return 'Second character is not 0'
    for i in range(2, 7):
        try:
            temp = int(student_GID[i])
        except:
            return 'Not numeric'
    return True


for student in student_list:
    if check_GID(student[0]) != True:
        print('%s. %s' % (student[0], check_GID(student[0])))

for student in student_list:
    print(student)
