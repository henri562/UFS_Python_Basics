a = 9
b = 21
c = 50

# basic if
if a == b:
    print('a is equal to b')
elif a > b:
    print('a is greater than b')
else:
    print('a is less than b')

# nested if
if c > b:
    if c > a:
        print('c is bigger than a and b')
    else:
        print('c is bigger than a but not bigger than b')

# if with and
if a > 12 and a < 20:
    print('a is more than 12 and less than 20')

# if with or and and
if b > a and b > c:
    print('b is the largest number')
elif b > a or b > c:
    print('b is not the smallest number')
else:
    print('b is the smallest number')

# not equal
if a != b and a != c and b != c:
    print('a, b and c are all different')
