def examination():
    sat = input('Did you sit the exam y/n:')
    if sat == 'y':
        exam = int(input('Enter your exam mark:'))
        if exam >= 83:
            statement = 'Your grade is an A'
        elif exam >= 70:
            statement = 'You grade is an B'
        elif exam >= 50:
            statement = 'You grade is an C'
        else:
            statement = 'Sorry you have not passed the exam'
    else:
        statement = 'Please provide an illness/misadventure form'

    return statement


print(examination())
