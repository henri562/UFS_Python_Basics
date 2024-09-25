from turtle import *


def draw_box():
    for i in range(4):
        forward(50)
        left(90)


draw_box()
right(180)
draw_box()
right(180)
penup()
left(45)
forward(70)
pendown()
backward(140)
