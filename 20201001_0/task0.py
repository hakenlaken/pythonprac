# Задача_0: поиск Парето-фронта в двумерном пространстве
def Pareto(inp):
    for i in range(len(inp)):
        j = 0
        while Flag := nodom(inp[i], inp[j]):
            j += 1
            if j == len(inp):
                break
        if Flag:
            print(inp[i], " ")


def nodom(x=(), y=()):
    if (x[0] > y[0]) or (x[1] > y[1]):
        return True
    elif (x[0] <= y[0]) and (x[1] <= y[1]):
        if x[0] >= y[0] and x[1] >= y[1]:
            return True
        else:
            return False


inp = eval(input())
Pareto(inp)
