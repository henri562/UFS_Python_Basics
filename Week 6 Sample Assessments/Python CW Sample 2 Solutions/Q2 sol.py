num = int(input('Please enter a postibve number less than 1000'))

if num < 10:
    print('1 digit')
elif num < 100:
    print('2 digit')
else:
    print('3 digit')
