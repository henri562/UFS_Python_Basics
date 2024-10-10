from turtle import *


# draws a square with sides of length pixels
def make_square(length):
    for i in range(4):
        forward(length)
        left(90)

def reposition():
    penup()
    right(90)
    forward(25)
    right(90)
    forward(25)
    right(180)
    pendown()

make_square(100)
reposition()
make_square(150)
reposition()
make_square(200)
reposition()
make_square(250)
done()
