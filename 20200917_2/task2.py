# Задача_2 (на while-else)
a = 0
c = a
while (b := int(input())) > 0:
    a += b
    if (a > 21):
        print(a)
        break
    c = b
else:
    print(int(c))
