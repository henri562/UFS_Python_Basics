age = input('Enter your age, using a number:')
if age != "":
    age = int(age)
    if age > 0:
        if age > 1:
            print('You are %s years old' % age)
        else:
            print('You cannot be that young')
    else:
        print('You must enter a numeric value greater than zero e.g. 5')
else:
    print('Maybe another time')
