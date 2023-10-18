from turtle import *

def draw_square(size):
   for i in range (0,4):
      forward(size)
      left(90)


draw_square(50)
penup()
forward(100)
pendown()
draw_square(100)

