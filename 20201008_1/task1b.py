# график функции: sin(x)
from math import sin
import decimal
height = 25
width = 80
decimal.getcontext().prec = 5
xleft = decimal.Decimal(str(-4))
xright = decimal.Decimal(str(4))
yleft = decimal.Decimal(str(-1))
yright = decimal.Decimal(str(1))
dely = decimal.Decimal(str(abs(yright - yleft) / (height)))
delx = decimal.Decimal(str(abs(xright - xleft) / (width)))
print(dely, delx)
iterx = xleft
L = []
stepx = 0
while iterx <= xright:
    stepy = int(height / 2) - int(decimal.Decimal(str(sin(iterx))) / dely)
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
