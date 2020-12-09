import sys


class dump(type):
    def __init__(self, *ap, **an):
        import types
        for attr, obj in vars(self).items():
            if isinstance(obj, types.FunctionType):
                def genf(f, name):
                    def newfun(self, *args, **kwargs):
                        print(name, ": ", args, ", ", kwargs, sep="")
                        res = f(self, *args, **kwargs)
                        return res
                    return newfun
                newf = genf(obj, attr)
                setattr(self, attr, newf)
        super().__init__(*ap, **an)

    # def __new__(metacl, name, parents, namespace):
    #    print("new:", name, parents, namespace)
    #    cls = super().__new__(metacl, name, parents, namespace)
    #    return cls

    # def __call__(self, *ap, **an):
        # print("call:", self, ap, an)
    #    super().__call__(*ap, **an)


exec(sys.stdin.read())
