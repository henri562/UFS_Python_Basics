"""
a program to accept user input, test if it is a number,
and then send if off to calculate the circumference and area of the circle.
"""

import math


# calculates the circumference of a circle, given the radius
def calculate_circ(radius):
    circumf = 2 * math.pi * radius
    return circumf


# calculates the area of a circle, given the radius
def calculate_area(radius):
    area = math.pi * radius ** 2
    return area


# A function to test if the input is a number
# Returns True or False
def isNumber(possNum):
    isNum = False
    try:
        n = float(possNum)
        isNum = True
    except:
        print('This is not a number')
    return isNum


print('Calculate the circumference and area of a circle')
user_input = input('Type in the radius in centimetres: ')
if isNumber(user_input) == False:
    exit()

# note that this works because user_input is known to be a number
# if user_input was not a number the code would have stopped running
radius = float(user_input)
print('%s is a number' % user_input)

# calculate and print circumference and area of circle
print('The circumference of the circle is %.4f centimetres.' % calculate_circ(radius))
print('The area of the circle is %.4f square centimetres.' % calculate_area(radius))
