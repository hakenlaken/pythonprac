from re import match

print(bool(match(r"(\+|-)?(\d*)?(\.|\.\d+)?((e|E)([+-])?\d+)?$", input())))
