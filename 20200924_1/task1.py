# Задача_1 простые числа в заданном диапазоне (однострочник!)
N = 100
l = [i for i in range(1, N) if all([i % d for d in range(2, i//2+1)])]
print(l)
