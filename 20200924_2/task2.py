# Задача_2 ввести и отсортировать числовой список, в качестве ключа сравнения использовать остаток от деление x ** 2 на 100
a = list(eval(input()))
for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if ((a[j] ** 2) % 100) < ((a[i] ** 2) % 100):
            a[i], a[j] = a[j], a[i]
print(a)