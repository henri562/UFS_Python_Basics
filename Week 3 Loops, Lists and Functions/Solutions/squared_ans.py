def square(n):
    '''
    **2 returns the square of a number
    it raises to the power of 2
    '''
    squared = n ** 2
    return squared


for i in range(3, 10, 2):
    print('The square of %d is %d.' % (i, square(i)))
