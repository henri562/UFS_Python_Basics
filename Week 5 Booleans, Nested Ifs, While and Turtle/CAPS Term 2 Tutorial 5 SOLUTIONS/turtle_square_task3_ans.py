from turtle import *


# draws a square with sides of length pixels
def make_square(length):
    for i in range(4):
        forward(length)
        left(90)


make_square(100)
make_square(150)
