from random import choice
sogl = "йцкнгшщзхфвпрлджчсмтб"
glas = "уеыаоэёяию"
list = ["0", "1", "2"]
N = int(input())
i = 0
while i < N:
    if N - i >= 2:
        randi = choice(list)
    else:
        randi = "0"
    if randi == "0":
        print(choice(glas), end="")
        i += 1
    elif randi == "1":
        print(choice(glas) + choice(sogl), end="")
        i += 2
    elif randi == "2":
        print(choice(sogl) + choice(glas), end="")
        i += 2
print()
