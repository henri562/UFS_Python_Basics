num = int(input('Enter  a number less than 100:'))
if num < 0:
    print('A negative number.')
elif num < 10:
    print('A one digit number')
elif num < 100:
    print('A two digit number.')
else:
    print('Must be a number less than one hundred.')
