from Brain import Brain

b = Brain(2, 4, 4, 5)

a = b.entscheide([0, 1, 0, 0])

print(a)
print(b.entscheide([0, 1, 1, 0]))
c = b.getGenetics()
print(c)
print(len(c))
c[0] = 21345647586
b.buildWithGenetics(c)
print(b.getGenetics())
