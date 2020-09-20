# Задача_4 (тоже на вложенные циклы while)
a = int(input())
n = int(input())
x = 1
flag = 0
while x <= (a / 3 + 1):
    xx = x ** n
    y = 1
    while y <= (a / 3 + 1):
        yy = y ** n
        z = 1
        axy = a - xx - yy
        while z <= (a ** (1 / n)):
            if z ** n == axy:
                print(x, y, z)
                flag = 1
                break
            z += 1
        if flag:
            break
        y += 1
    if flag:
        break
    x += 1
if not flag:
    print("FAIL")
