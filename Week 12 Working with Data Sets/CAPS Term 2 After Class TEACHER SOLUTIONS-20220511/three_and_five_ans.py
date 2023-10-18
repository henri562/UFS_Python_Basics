"""
A program to find all the numbers that are divisible only by both 3 and 5
"""


# tests if a number is divisible by a divisor or not
# returns True or False
def is_divisible(num, divisor):
    if num % divisor == 0:
        return True
    else:
        return False


# work out the number of factors divide into a number
def num_factors(numb, div):
    # already known to be divisible by 3 and 5
    factor = 0
    while numb % div == 0:
        factor += 1
        # print('factor 3')
        numb = numb / div
    return factor


max_number = 1000
counter = 0
print('Numbers divisible by 3 and 5 only, under %d.' % max_number)
for i in range(1, max_number + 1):
    if is_divisible(i, 3) == True and is_divisible(i, 5) == True:
        if 3 ** num_factors(i, 3) * 5 ** num_factors(i, 5) == i:
            print(str(i) + ' = ', end='')
            print(' 3^%d' % num_factors(i, 3), end='')
            print(' x 5^%d' % num_factors(i, 5))
            counter += 1

print('There are %d numbers under %s that are divisible only by 3 and 5'
      % (counter, max_number))
