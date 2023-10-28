"""
draw two pairs of boxes
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


draw_box(100, 200, 'green')

pu()
fd(100)
rt(90)
pd()

draw_box(50, 150, 'red')
done()

