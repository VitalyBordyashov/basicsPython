from functools import reduce
c = [x for x in range(100, 1001) if x % 2 == 0]
p_all = reduce(lambda x,y: x * y, c)
print(c)
print(p_all)
