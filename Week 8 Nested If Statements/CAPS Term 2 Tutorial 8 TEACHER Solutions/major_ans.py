def majors():
    # major = input('What is your major ?').lower()
    major = input('What is your major? ')
    major = major.lower()
    if major == 'science':
        semester = int(input('What is the semester 1/2? '))
        if semester == 2:
            statement = 'Great we have programming'
        else:
            statement = 'Maybe next semester we have programming'
    else:
        statement = 'Sorry you are not a science student'
    return statement


print(majors())
