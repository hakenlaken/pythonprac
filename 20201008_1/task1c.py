# график функции
from math import *
func = input()
a, b, c, d = input().split(",")


def f(x):
    return eval(func)


height = 25
width = 80
xleft = float(a)
xright = float(b)
yleft = float(c)
yright = float(d)
dely = (yright - yleft) / (height)
delx = (xright - xleft) / (width)
iterx = xleft
L = []
stepx = 0
while iterx <= xright:
    if iterx == 0:
        iterx = 0.000000001
    stepy = int(height / 2 - (f(iterx)) / dely)
    L.append((stepy, stepx))
    stepx += 1
    iterx += delx
for i in range(height):
    for j in range(width):
        if (i, j) in L:
            print("*", end='')
        else:
            print(" ", end='')
    print()
