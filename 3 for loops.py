# while indefinite iteratione
# for definite iteratione

a = {'a': 1, 'b': 2, 'c': 3}
for i in a:
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)
for i, j in a.items():
    print(i, j)

# iter() agar error nade yani  iterable e
# next() agar error nade yani iterator e

for n in range(10, 20, 2):
    print(n)

for i in range(10):
    if i % 3 == 0:
        continue
    print(i)

# continue o break o else tu for
# ham hastand
# pass ham tu for hast


for i in range(1000):
    pass
print('for loop passed')

# while pass nadare chon code
# ta binahayat mire
