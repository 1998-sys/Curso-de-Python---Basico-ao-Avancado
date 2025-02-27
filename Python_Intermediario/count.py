# Count é um iterador sem fim (itertools)

from itertools import count

c1 = count()

r1 = range(10)

print(next(c1))
print(next(c1))

for i in c1:
    if i > 100 :
        break

    print(i)