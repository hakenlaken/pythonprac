# написать декоратор который считает количество вызовов функции и выводит его (с использованием глобальной переменной)
from functools import wraps
import sys


def deccount(f):
    counter = 0

    @wraps(f)
    def newfun(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(counter)
        return f(*args, **kwargs)
    return newfun


exec(sys.stdin.read())
