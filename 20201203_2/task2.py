def check_annotations(self):
    for attr, obj in self.__annotations__.items():
        if not hasattr(self, attr) or not isinstance(getattr(self, attr), obj):
            return False
    return True


class check(type):

    def __init__(self, *ap, **an):
        setattr(self, "check_annotations", check_annotations)
        super().__init__(*ap, **an)


class C(metaclass=check):
    A: int
    B: str = "QQ"


c = C()
print(c.check_annotations())
c.A = "ZZ"
print(c.check_annotations())
c.A = 100500
print(c.check_annotations())
c.B = type("Boo", (str,), {})(42)
print(c.check_annotations())
