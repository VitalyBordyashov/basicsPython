main_str = input("Введите несколько слов через пробел")
s = main_str.split(" ")
print(s)
for ind, el in enumerate(s, 1):
    if len(el) > 10:
        string = list(el)
        i = 10
        while i < len(string):
            string.pop(i)
        el = ("".join(string))
    print(ind, el)