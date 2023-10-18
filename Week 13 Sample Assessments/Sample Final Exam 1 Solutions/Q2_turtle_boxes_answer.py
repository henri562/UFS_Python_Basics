"""
draw two pairs of boxes inside boxes
"""
# note that you need to use begin_fill and end_fill each time
# otherwise fill may not work.

from turtle import *


def draw_box(width, height, colour):
    fillcolor(colour)
    begin_fill()
    for i in range(2):
        fd(width)
        lt(90)
        fd(height)
        lt(90)
    end_fill()


def reposition_turtle(distance, angle):
    pu()
    fd(distance)
    lt(angle)
    fd(distance)
    rt(angle)
    pd()


# draw outer rectangular box
draw_box(100, 200, 'green')

# reposition turtle cursor
reposition_turtle(25, 90)

# draw inner rectangular box
draw_box(50, 150, 'yellow')

# keep turtle window open
done()
