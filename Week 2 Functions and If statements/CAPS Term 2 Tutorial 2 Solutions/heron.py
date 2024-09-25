# Write a program which reads the side lengths a, b and c of a triangle,
# and computes the area of the triangle using Heron's formula:
# area = sqrt(s(s-a)(s-b)(s-c))
# s = (a + b + c)/2
# Note: Not all combinations of 3 numbers can be the sides of a triangle
# but you may assume for this exercise, only valid lengths for a triangle are
# entered

import math
a=float(input('Please enter the length of side 1: '))
b=float(input('Please enter the length of side 2: '))
c=float(input('Please enter the length of side 3: '))
s=(a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))          
print('Area = %.2lf' %area)
