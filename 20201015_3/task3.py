from random import seed, choices, choice
import sys
import urllib.request
fhand = urllib.request.urlopen(
    'http://uneex.org/LecturesCMC/PythonIntro2020/06_DictCollection?action=AttachFile&do=get&target=anna.txt').read().decode().lower()
if len(sys.argv) > 2:
    S = int(sys.argv[2])
else:
    S = 100500
seed(S)
N = int(sys.argv[1])

flagchar = False
cleft = None
D = {}
for c in fhand:
    if not flagchar and c.isalpha():
        flagchar = True
        cleft = c
    elif flagchar and c.isalpha():
        D[cleft + c] = D.get(cleft + c, 0) + 1
        flagchar = True
        cleft = c
    else:
        flagchar = False
if N == 1:
    S = choices(list(D), weights=D.values(), k=1)
    print(S[0][0])
    exit()
Di = D
for i in range(N - 1):
    S = choices(list(Di), weights=Di.values(), k=1)
    print(S[0], end="")
    Di = {}
    if i == 0:
        lastchar = S[0][1]
    else:
        lastchar = S[0]
    for i in D.keys():
        if i[0] == lastchar:
            Di[i[1]] = D[i]
print()
