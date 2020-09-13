s = input("Give me a name and I'll give you ACCII number: ")
hash = 0
for c in s:
    hash += ord(c)
print(hash)
