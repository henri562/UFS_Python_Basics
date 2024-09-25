# a function that multiplies two numbers

def multiply(a, b):
    product = a * b
    statement = '%d x %d = %d' % (a, b, product)
    return statement


num1 = int(input('Please enter a number: '))
num2 = int(input('Please enter another number: '))
print(multiply(num1, num2))
