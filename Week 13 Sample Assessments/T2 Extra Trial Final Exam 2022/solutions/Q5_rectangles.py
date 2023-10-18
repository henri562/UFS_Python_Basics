from turtle import *


def rectangle(w, h):
    for i in range(2):
        fd(w)
        lt(90)
        fd(h)
        lt(90)


w = 300
h = 200
gap = 13
while gap > 5:
    rectangle(w, h)
    pu()
    lt(90)
    fd(gap)
    rt(90)
    fd(gap)
    pd()
    w = w * 0.9
    h = h * 0.9
    gap = gap * 0.9
