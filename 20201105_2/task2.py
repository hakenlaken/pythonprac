from re import sub
print(sub(r"([aeiouy])([^aeiouy]*)?([aeiouy])", r"\3\2\1", input(), count=1))
