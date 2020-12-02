word = input()
newword = ""
for a in word:
    try:
        newword += a.encode("latin1").decode("cp1251")
    except UnicodeEncodeError:
        newword += "?"

print(newword)
