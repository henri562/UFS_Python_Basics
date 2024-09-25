# draw 4 colourful stars that do no overlap
# using a loop
# note: this is not the only way to do this.

from turtle import *

pencolor('red')
fillcolor('yellow')


def draw_star(points):
    begin_fill()
    for i in range(points):
        forward(100)
        right(180 - 180 / points)
    end_fill()


x = -100
y = -100

for i in range(4):
    penup()
    setpos(x, y)
    pendown()
    draw_star(i * 2 + 5)
    x *= -1
    if i == 1:
        y += 200
