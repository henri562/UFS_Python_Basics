import turtle
from turtle import *

shape('turtle')


steps = 200
x = 200
y = 100
angle = 90


def teleport():
    pu()
    fd(steps)
    pd()
    turtle.done()


# goto(50, 100)

# print(turtle.tracer(0))
turtle.tracer(2)

for i in range(3):
    fd(x)
    lt(angle)
fd(x)


turtle.done()
