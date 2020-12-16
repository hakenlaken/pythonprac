import asyncio
Src = eval(input())


async def merge(data):
    lenn = len(data)
    if lenn > 2:
        head = asyncio.create_task(merge(data[:lenn // 2]))
        tail = asyncio.create_task(merge(data[lenn // 2:]))
        await asyncio.gather(head, tail)
        data = head.result() + tail.result()
        for i in range(0, lenn - 1):
            min = data[i]
            index = i
            for j in range(i + 1, lenn):
                if min > data[j]:
                    min = data[j]
                    index = j
            if index != i:
                data[i], data[index] = data[index], data[i]
    elif lenn > 1 and data[0] > data[1]:
        data[0], data[1] = data[1], data[0]
    return data

Res = asyncio.run(merge(Src))
print(Res)
