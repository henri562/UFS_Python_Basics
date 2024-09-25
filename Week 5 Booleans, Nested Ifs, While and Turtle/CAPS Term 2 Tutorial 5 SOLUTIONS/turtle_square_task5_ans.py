from turtle import *


# draws a square with sides of length pixels
def make_square(length):
    for i in range(4):
        forward(length)
        left(90)


for i in range(3):
    make_square(i * 50 + 100)

    penup()
    right(90)
    forward(25)
    right(90)
    forward(25)
    right(180)
    pendown()
