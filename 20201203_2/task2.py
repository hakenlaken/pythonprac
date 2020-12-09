import sys


def check_annotations(self):
    for attr, obj in self.__annotations__.items():
        if not hasattr(self, attr) or not isinstance(getattr(self, attr), obj):
            return False
    return True


class check(type):

    def __init__(self, *ap, **an):
        setattr(self, "check_annotations", check_annotations)
        super().__init__(*ap, **an)


exec(sys.stdin.read())
