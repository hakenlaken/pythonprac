# ввести 3 числа через запятую, проверить является ли треугольником
a, b, c = eval(input())
if (a + b > c) and (a + c > b) and (b + c > a) and (a > 0) and (b > 0) and (c > 0):
    print("Triangle")
else:
    print("Not Triangle")
