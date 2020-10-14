N, M = eval(input())
List = list(range(1, N + 1))
lenN = len(str(N))
lenNN = len(str(N ** 2))
x = int((M + 3) / (9 + 2 * len(str(N)) + len(str(N ** 2))))
if x == 0:
    print("too low M for such N")
    quit()
while len(List) > 0:
    print("=" * M)
    current = List[0:x]
    if len(List) < x:
        x = len(List)
    for i in range(1, N + 1):
        for j in current:
            if j != current[len(current) - 1]:
                print("{1:>{2}} * {0:<{2}} = {4:<{3}}".format(i, j, lenN, lenNN, i * j), end=' | ')
            else:
                print("{1:>{2}} * {0:<{2}} = {4:<{3}}".format(i, j, lenN, lenNN, i * j))
    List = List[x:]
print("=" * M)
