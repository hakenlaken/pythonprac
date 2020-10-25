def fib(a, b):
    x1 = 1
    x2 = 1
    for i in range(0, a - 1):
        x = x2
        x2 = x2 + x1
        x1 = x
    for i in range(a, b + 1):
        yield x1
        x = x2
        x2 = x2 + x1
        x1 = x


a, b = eval(input())
print(*fib(a, b))
