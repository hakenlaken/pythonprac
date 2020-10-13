# Заданы два многочлена от х (А(х), В(х)) с рациональными коэффициентами, а также рациональные числа s и w. Проверить, является ли s решением уравнения A(x)/B(x)=w
from fractions import Fraction as F
inp = input()
mas = inp.split(", ")

s = F(mas[0])
w = F(mas[1])
stepA = int(mas[2])
masa = mas[3:3 + stepA + 1]
masA = []
for i in range(0, stepA + 1):
    x = F(masa[i])
    masA.append(x)
stepB = int(mas[3 + stepA + 1])
masb = mas[(3 + stepA + 2):]
masB = []
for i in range(0, stepB + 1):
    x = F(masb[i])
    masB.append(x)


def Fun(x, w, A, B):
    sum1 = sum(x**(len(A) - i - 1) * c for i, c in enumerate(A))
    sum2 = sum(x**(len(B) - i - 1) * c for i, c in enumerate(B))
    return sum2 * w == sum1


print(Fun(s, w, masA, masB))
