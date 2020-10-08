# Заданы два многочлена от х (А(х), В(х)) с рациональными коэффициентами, а также рациональные числа s и w. Проверить, является ли s решением уравнения A(x)/B(x)=w
from fractions import Fraction as F
inp = input()
mas = inp.split(", ")

s = F(mas[0])
print(s)
w = F(mas[1])
print(w)
stepA = int(mas[2])
masa = mas[3:3 + stepA + 1]
masA = []
print(masa[0], masa[1], masa[2])
for i in range(0, stepA + 1):
    x = F(masa[i])
    masA.append(x)
print(masA)
stepB = int(mas[3 + stepA + 1])
print(stepB)
print(mas[(3 + stepA + 3)])
masb = mas[(3 + stepA + 2):]
masB = []
for i in range(0, stepB + 1):
    x = F(masb[i])
    masB.append(x)


def Fun(x, w, A, B):
    sum1 = sum(x**(len(A) - i - 1) * c for i, c in enumerate(A))
    sum2 = sum(x**(len(A) - i - 1) * c for i, c in enumerate(A))
    return sum2 * w == sum1


print(Fun(s, w, masA, masB))
print()
