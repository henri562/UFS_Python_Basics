# draw 4 colourful stars that do no overlap

from turtle import *

pencolor('red')
fillcolor('yellow')

def draw_star(points):
    begin_fill()
    for i in range(points):
        forward(100)
        right(180-180/points)
    end_fill()

draw_star(5)
penup()
setpos(150,0)
pendown()
draw_star(5)
penup()
setpos(0,150)
pendown()
draw_star(5)
penup()
setpos(150, 150)
pendown()
draw_star(5)
