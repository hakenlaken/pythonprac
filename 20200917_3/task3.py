# Задача_3 (на вложенные циклы while)
i = 3
while i <= 6:
    j = 3
    while j <= 6:
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
        j += 1
    print()
    i += 1
