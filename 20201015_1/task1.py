inp = input().lower()
flagchar = False
cleft = None
D = {}
for c in inp:
    if not flagchar and c.isalpha():
        flagchar = True
        cleft = c
    elif flagchar and c.isalpha():
        D[cleft + c] = D.get(cleft + c, 0) + 1
        flagchar = True
        cleft = c
    else:
        flagchar = False

print(len(D.keys()))
