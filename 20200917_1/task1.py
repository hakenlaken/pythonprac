# Задача_1 (на if-ы)
a = int(input())
if a % 2 != 0 and a % 25 == 0:
    print("B+ ", end='')
    print("A- ", end='')
elif a % 25 == 0:
    print("B- ", end='')
    print("A+ ", end='')
else:
    print("B- ", end='')
    print("A- ", end='')
if a % 8 == 0:
    print("C+ ")
else:
    print("C- ")
