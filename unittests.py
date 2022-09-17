from Brain import Brain

b = Brain(4, 8, 4, 5)

a = b.entscheide([0, 1, 0, 0])

print(a)
print(len(a))

c = b.getGenetics()
print(c)
print(len(c))

c[0] = 123
b.buildWithGenetics(c)
print("Done successfully")
print(b.getGenetics())