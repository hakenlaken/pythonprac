# Задача_3 (на цикл for)
for i in range(3, 7):
    for j in range(3, 7):
        n = i * j
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit
            n //= 10
        if sum == 6:
            print(':=)', end=' ')
        else:
            print(i * j, end=' ')
    print()
