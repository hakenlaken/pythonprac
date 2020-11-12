class nestr(str):
    def __neg__(self):
        return self.__class__("".join(reversed(self.data)))

    def __add__(self, other):
        if isinstance(other, nestr):
            return self.__class__(self.data + other.data)
        elif isinstance(other, str):
            return self.__class__(self.data + other)
        return self.__class__(self.data + str(other))

    def __init__(self, seq):
        if isinstance(seq, str):
            self.data = seq
        elif isinstance(seq, nestr):
            self.data = seq.data[:]
        else:
            self.data = str(seq)

    def __str__(self):
        return str(self.data)


Expr = input()
print(eval(Expr))
