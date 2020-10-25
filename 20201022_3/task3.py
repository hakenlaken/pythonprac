from itertools import filterfalse, product
# map - - продукт в строчку
filterfalse(lambda x: x.count() == 2, list(map("".join, (product('TOR', repeat=7)))))
