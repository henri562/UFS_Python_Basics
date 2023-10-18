from turtle import *

# draws a square with sides of length pixels
def make_square(length):
    for i in range(4):
        forward(length)
        left(90)

original_length=20

for i in range(9):
    side_length=original_length*i
    make_square(side_length)

    penup()
    right(90)
    forward(original_length/2)
    right(90)
    forward(original_length/2)
    right(180)
    pendown()


