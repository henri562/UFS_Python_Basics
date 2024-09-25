'''
A function that adds two numbers
and returns the result as a string
'''


def add(a, b):
    total = a + b
    statement = 'The sum of %d and %d is %d.' % (a, b, total)
    return statement


num1 = int(input('Please enter a number: '))
num2 = int(input('Please enter another number: '))
print(add(num1, num2))
