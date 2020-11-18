from random import random, randint, randrange
c = [randint(0, 100) for _ in range(10)]
print(c)
a = []
i = 0
while i < len(c):
    m = c[i]
    if c[i + 1] > m:
        a.append(c[i + 1])
    i += 2
print(a)

