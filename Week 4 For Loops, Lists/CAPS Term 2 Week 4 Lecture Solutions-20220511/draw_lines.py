import turtle
from turtle import *

length = 0
for i in range(4):
    length += 50
    left(90)
    forward(length)
    back(length)
    right(90)
    penup()
    forward(50)
    pendown()