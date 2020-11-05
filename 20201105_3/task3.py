from re import search, sub
a = input()
print(search(r"(?<=[0]+)[0-9]{2,5}(?=[0]+)", a))
print(search(r"(?<=([0]+))[0-9]$", a))
