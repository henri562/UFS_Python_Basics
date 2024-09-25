'''
A function that adds two numbers
and returns the result as a string
'''


def add(a, b):
    total = a + b
    statement = 'The sum of %d and %d is %d.' % (a, b, total)
    return statement


print(add(4, 5))
