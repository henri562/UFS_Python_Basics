from turtle import *


def draw_shape(side, filled):
    if filled == True:
        begin_fill()
        fillcolor('blue')
    for i in range(8):
        forward(side)
        left(45)
    end_fill()
    print()


length = 50
draw_shape(length, True)
penup()
forward(150)
pendown()
draw_shape(length / 2, False)
done()
