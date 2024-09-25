"""
Code to produce 1 2 4 8 16 etc
9 elements long
"""

num = 1
r = 9
for i in range(r):
    print(num, end='')
    if i < r - 1:
        print(', ', end='')
    else:
        print('.')
    num *= 2  # multiply preceding number by two

print()

# alternative answer
for i in range(r):
    print('%d' % 2 ** i, end='')  # raise 2 to the power of i
    if i < r - 1:
        print(', ', end='')
    else:
        print('.')
