# Задана строка из пар вида (буква, последовательность цифр). В ней используются буквы A, B, C и цифры 1, 2, 3, 4, 5; например: "A12B2425C543A21B4". Корректность строки гарантирована. Требуется: для каждого вхождения B вывести номер (позицию в строке) последней из цифр, следующих за B, и саму эту цифру.
a = input()
flagB = 0
for n, i in enumerate(a):
    if (i == "B") and flagB:
        print(n - 1, a[n - 1])
    if (i == "A" or i == "C") and flagB:
        print(n - 1, a[n - 1])
        flagB = 0
    if i == "B":
        flagB = 1
if flagB:
    print(n, a[n])