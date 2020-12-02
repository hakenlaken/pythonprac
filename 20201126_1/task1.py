# bswap.py файл поменять местами половинки бинарного файла
import sys

N = int(sys.stdin.buffer.read(2))


data = sys.stdin.buffer.read()
datalist = []
for i in range(0, N):
    datalist.append(data[i * (len(data) // N): (i + 1) * (len(data) // N)])
datalist = sorted(datalist)

for i in range(0, N):
    sys.stdout.buffer.write(datalist[i])
