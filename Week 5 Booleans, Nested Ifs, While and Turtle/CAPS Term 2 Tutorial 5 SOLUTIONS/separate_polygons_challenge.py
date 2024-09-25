from turtle import *


def draw_polygon(num_sides):
    for i in range(num_sides):
        forward(int(180 / num_sides))
        left(360 / num_sides)


# a program that draws 9 non-overlapping polygons with 3 to 12 sides
pencolor('red')
fillcolor('yellow')
xpos = 0
ypos = 0
for sides in range(3, 12):
    penup()
    # after drawing 3 move x back to zero
    if xpos == 3:
        xpos = 0
    if sides == 6 or sides == 9:
        ypos += 1
    print('%s, %s' % (xpos * 100, ypos * 100))
    setpos(xpos * 100, ypos * 100)
    pendown()
    begin_fill()
    draw_polygon(sides)
    end_fill()
    # increase xpos for the next draw
    xpos += 1
