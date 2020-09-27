# Ввести строки (конец ввода — пустая строка). Выввести (в порядке ввода) только те строки, все символы которых не встречаются в других введённых строках.
dictionary = set()
doubledic = set()
words = []
while inp := input():
    word = set(inp)
    doubledic.update(word & dictionary)
    dictionary.update(word)
    words.append(inp)
for wordi in words:
    if not set(wordi) & doubledic:
        print(wordi)
