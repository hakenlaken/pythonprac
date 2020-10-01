# Задача_1: написать функцию вычитания двух объектов
def fun(a, b):
    if type(a) is str:
        res = ""
        for d in [c for c in a if c not in b]:
            res += d
        return res
    elif hasattr(a, "__sub__"):
        return a - b
    else:
        return type(a)(c for c in a if c not in b)


inp = eval(input())
print(fun(inp[0], inp[1]))
