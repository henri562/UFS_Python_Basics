'''
An alternative version of drawing polygons
'''

from turtle import *

# a program that draws 9 non-overlapping polygons with 3 to 12 sides
# it draws in red and fills objects with yellow
color('red', 'yellow')
for j in range(3, 12):
    penup()
    xpos = (j - 3) % 3
    ypos = int(j / 3) - 1
    # print(str(xpos*100) + ', ' + str(ypos*100))
    setpos(xpos * 100, ypos * 100)
    pendown()

    begin_fill()

    for i in range(0, j):
        forward(int(180 / j))
        left(360 / j)

    end_fill()
