"""
a program to accept user input, test if it is a number,
and then send it off to calculate the surface area
and volume of a sphere with the given radius
"""

import math


# calculates the surface are of a sphere, given the radius
def calculate_surface(radius):
    surface = 4 * math.pi * radius ** 2
    return surface


# calculates the volume of a sphere, given the radius
def calculate_volume(radius):
    volume = 4 / 3 * math.pi * radius ** 3
    return volume


# A function to test if the input is a number
# Returns True or False
def is_number(poss_num):
    is_num = False
    try:
        n = float(poss_num)
        is_num = True
    except:
        print('This is not a number')
    return is_num


print('Calculate the surface area and volume of a sphere')
user_input = input('Type in the radius in centimetres: ')
if is_number(user_input) == False:
    exit()
radius = float(user_input)
print('The surface area of the sphere is %.2f square centimetres.' % calculate_surface(radius))
print('And the volume of the sphere is %.2f cubic centimetres.' % calculate_volume(radius))
