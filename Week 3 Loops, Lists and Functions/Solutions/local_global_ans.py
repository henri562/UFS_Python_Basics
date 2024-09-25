'''
Code that illustrates global and local variables
'''

# global variable
number = 0
statement = 'Hello'
print('The value of number is %d' % number)
print('The value of statement is %s' % statement)


def multiply(num1, num2):
    # print global variable
    print('In the function, global variable number is %d.' \
          % number)
    # local variable
    product = num1 * num2
    statement = 'The value of the local variable product is %d.' % product
    return statement


print(multiply(10, 20))
print('After the function, the value of the global variable number is still %d.' \
      % number)
print('The original variable statement still has the value %s.' % statement)
