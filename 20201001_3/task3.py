def Calc(a, b, c):
    def fnew(x):
        m = eval(a)
        n = eval(b)
        x = m
        y = n
        return eval(c)
    return fnew
