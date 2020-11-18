def fact(n):
    i = 1
    f = 1
    while i <= n:
        f = f * i
        i += 1
        yield f
s = [bullet for bullet in fact(5)]
c = {f"{str(k)}!": v for k, v in enumerate(fact(5))}
print(s)
print(c)