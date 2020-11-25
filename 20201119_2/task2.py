# дескриптор хранит только числа, если нужно было не число
import sys


class Num:
    def __get__(self, obj, cls):
        try:
            return obj._value
        except:
            return 0

    def __set__(self, obj, val):
        if hasattr(val, "__int__"):
            obj._value = val.conjugate()
        elif hasattr(val, "__len__"):
            obj._value = len(val)
        else:
            obj._value = 0


exec(sys.stdin.read())
