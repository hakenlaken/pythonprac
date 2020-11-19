# дескриптор хранит только числа, если нужно было не число
import sys


class Dsc:
    def __get__(self, obj, cls):
        return obj._value

    def __set__(self, obj, val):
        try:
            if hasattr(val, "__int__"):
                obj._value = val.conjugate()
            else:
                obj._value = len(val)
        except Exception:
            print("bad input")


class C:
    data = Dsc()

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"<{self.name}>"


exec(sys.stdin.read())
