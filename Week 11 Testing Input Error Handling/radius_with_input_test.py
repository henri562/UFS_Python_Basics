# a program to accept user input, test if it is a number,
# and then send if off to calculate the circumference and area of the circle.

# We have imported the math library as you will need to use math.pi 
# in some of your calculations
import math


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


print('Calculate the circumference and area of a circle')
user_input = input('Type in the radius in centimetres: ')
if is_number(user_input) == False:
    exit()
print('%s is a number.' % user_input)
