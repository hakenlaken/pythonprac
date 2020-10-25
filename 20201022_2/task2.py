from itertools import islice, filterfalse, tee


def even(seq):
    return filterfalse(lambda x: x % 2, seq)


def slide(seq):
    seq = iter(seq)
    while True:
        s, seq = tee(seq, 2)
        win = list(islice(s, 3))
        if len(win) < 3:
            return
        yield from even(win)
        next(seq)


seq = eval(input())
print(*slide(seq))
