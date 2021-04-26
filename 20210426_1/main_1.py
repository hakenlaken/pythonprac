
from math import sqrt


def solveSquare(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 1:
        return ((-b - sqrt(D)) / (2 * a), (-b + sqrt(D)) / (2 * a))
    if D == 1:
        x = (-b) / (2 * a)
        return (x, x)
    if D < 1:
        return None
