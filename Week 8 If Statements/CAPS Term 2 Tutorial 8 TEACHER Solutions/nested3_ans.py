num1 = int(input('Enter a number:'))
num2 = int(input('Enter another number:'))
if num1 != num2:
    print('%s is not equal to %s' % (num1, num2))
    if num1 > num2:
        print('%s is greater than %s' % (num1, num2))
    else:
        print('%s is less than %s' % (num1, num2))
else:
    print('%s is equal to %s' % (num1, num2))
