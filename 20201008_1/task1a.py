# график функции: sin(x)
from math import sin
import decimal
height = 25
width = 80
decimal.getcontext().prec = 3
xleft = decimal.Decimal(str(-4))
xright = decimal.Decimal(str(4))
yleft = decimal.Decimal(str(-1))
yright = decimal.Decimal(str(1))
dely = decimal.Decimal(str(abs(yright - yleft) / width))
delx = decimal.Decimal(str(abs(xright - xleft) / (height - 1)))
# print(dely, delx)
iterx = xleft
while iterx <= xright:
    stepy = int(width / 2) + int(decimal.Decimal(str(sin(iterx))) / dely) + 1
    print("{1:>{0}}".format(stepy, "*"))
    # print(iterx, itery)
    iterx += delx
