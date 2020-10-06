def Bisect(a, b):
    j = len(b) // 2
    if a == b[j] or len(b) == 1:
        if a == b[j]:
            return True
        else:
            return False
    elif a < b[j]:
        return Bisect(a, b[:j])
    else:
        return Bisect(a, b[j:])
