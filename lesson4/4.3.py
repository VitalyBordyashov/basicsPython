a = [x for x in range(20, 241, 20)]
print(a)
b = [x for x in range(21, 241, 21)]
print(b)
c = [x for x in range(240) if x // 21 and (x % 21 == 0)]
print(c)