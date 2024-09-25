from turtle import *

step_height = 50
num_steps = 4

forward(step_height * num_steps)
left(90)
forward(step_height * num_steps)
left(90)
for i in range(num_steps):
    forward(step_height)
    left(90)
    forward(step_height)
    right(90)
right(180)
